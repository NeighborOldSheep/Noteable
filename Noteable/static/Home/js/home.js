//mobile device menue-btn
const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector(".nav");

menuBtn.addEventListener("click", () => {
    nav.classList.toggle("mobile-menu");
    /* var menu = document.querySelector(".mobile-menu");
    menu.style.height = "100vh"; */
});
