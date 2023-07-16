const openMenu = document.getElementById("open-menu");
const closeMenu = document.getElementById("close-menu");
const nav = document.getElementById("nav");

openMenu.addEventListener("click",()=>{
    nav.classList.toggle("open");
    window.onscroll = ()=>{
        window.scrollTo(0,0);
    }
})

closeMenu.addEventListener("click",()=>{
    if(nav.hasAttribute("class")){
        nav.classList.toggle("open");
        window.onscroll=()=>{};
    }
})
