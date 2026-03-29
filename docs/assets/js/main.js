(function(){'use strict';
document.querySelectorAll('a[href^="#"]').forEach(a=>{
a.addEventListener('click',function(e){
const t=document.querySelector(this.getAttribute('href'));
if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'});}});});})();