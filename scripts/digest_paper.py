#!/usr/bin/env python3
"""
digest_paper.py — Generate a paper digest from a PDF using an LLM.

Requires an API key for the configured provider. Set one of:
  - ANTHROPIC_API_KEY (for Claude)
  - OPENAI_API_KEY (for GPT)
  - GEMINI_API_KEY (for Gemini)

Usage:
    python scripts/digest_paper.py --pdf path/to/paper.pdf --stream utility-decision-quality
    python scripts/digest_paper.py --pdf paper.pdf --stream agents-as-advisors --provider anthropic
"""

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
PAPERS_DIR = ROOT / "content" / "papers"

VALID_STREAMS = [
    "belief-elicitation",
    "uncertainty-communication",
    "utility-decision-quality",
    "attention-memory-salience",
    "risk-ambiguity",
    "temporal-dynamics",
    "sampling-representation",
    "agents-as-advisors",
]

VALID_PROVIDERS = ["anthropic", "openai", "gemini"]


def load_prompt() -> str:
    prompt_path = PROMPTS_DIR / "digest_prompt.md"
    if not prompt_path.exists():
        print(f"Error: Digest prompt not found at {prompt_path}")
        sys.exit(1)
    return prompt_path.read_text()


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text from PDF. Tries multiple backends."""
    try:
        import fitz  # PyMuPDF

        doc = fitz.open(str(pdf_path))
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except ImportError:
        pass

    try:
        import pdfplumber

        text = ""
        with pdfplumber.open(str(pdf_path)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except ImportError:
        pass

    print("Error: No PDF extraction library found.")
    print("Install one of: pip install PyMuPDF  OR  pip install pdfplumber")
    sys.exit(1)


def call_anthropic(system_prompt: str, user_content: str) -> str:
    import anthropic

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    return message.content[0].text


def call_openai(system_prompt: str, user_content: str) -> str:
    from openai import OpenAI

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        max_tokens=4096,
    )
    return response.choices[0].message.content


def call_gemini(system_prompt: str, user_content: str) -> str:
    import google.generativeai as genai

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        f"{system_prompt}\n\n---\n\n{user_content}",
    )
    return response.text


PROVIDERS = {
    "anthropic": call_anthropic,
    "openai": call_openai,
    "gemini": call_gemini,
}


def detect_provider() -> str:
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic"
    if os.environ.get("OPENAI_API_KEY"):
        return "openai"
    if os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
        return "gemini"
    return ""


def main():
    parser = argparse.ArgumentParser(description="Generate a paper digest from PDF using LLM")
    parser.add_argument("--pdf", required=True, type=Path, help="Path to PDF file")
    parser.add_argument("--stream", required=True, choices=VALID_STREAMS, help="Primary stream")
    parser.add_argument("--provider", choices=VALID_PROVIDERS, default=None, help="LLM provider")
    parser.add_argument("--output", type=Path, default=None, help="Output path (default: auto)")
    parser.add_argument("--max-chars", type=int, default=80000, help="Max chars of PDF text to send")
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"Error: PDF not found: {args.pdf}")
        return

    provider = args.provider or detect_provider()
    if not provider:
        print("Error: No API key found. Set ANTHROPIC_API_KEY, OPENAI_API_KEY, or GEMINI_API_KEY.")
        return

    print(f"Provider: {provider}")
    print(f"PDF: {args.pdf}")
    print(f"Stream: {args.stream}")

    # Extract text
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(args.pdf)
    if not text.strip():
        print("Error: No text extracted from PDF.")
        return
    print(f"  Extracted {len(text)} chars")

    # Truncate if needed
    if len(text) > args.max_chars:
        text = text[: args.max_chars]
        print(f"  Truncated to {args.max_chars} chars")

    # Build prompt
    system_prompt = load_prompt()
    user_content = (
        f"Please generate a structured paper digest for the following paper.\n"
        f"Primary stream: {args.stream}\n\n"
        f"--- PAPER TEXT ---\n\n{text}"
    )

    # Call LLM
    print("Generating digest (this may take a moment)...")
    call_fn = PROVIDERS[provider]
    result = call_fn(system_prompt, user_content)

    # Determine output path
    if args.output:
        out_path = args.output
    else:
        # Try to extract ID from the generated content
        out_path = PAPERS_DIR / "draft_digest.md"

    out_path.write_text(result)
    print(f"\nDraft digest written to: {out_path}")
    print("\nIMPORTANT: Review and edit the draft before committing.")
    print("Steps:")
    print(f"  1. Review and edit: {out_path}")
    print(f"  2. Rename to content/papers/{{id}}.md")
    print(f"  3. Add entry to data/papers.yaml")
    print(f"  4. Run: python scripts/build_site.py")


if __name__ == "__main__":
    main()
