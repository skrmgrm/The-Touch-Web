//js codes here

const menu = document.querySelector(".menu");
const menuIcon = document.querySelector(".menu-icon");
const nav = document.querySelector(".nav");
const socials = document.querySelector(".socials");

menu.addEventListener("click", () => {
    nav.classList.toggle("active");
    socials.classList.toggle("active");

    if (nav.classList.contains("active")) {
        menuIcon.classList.add("fa-times");
        menuIcon.classList.remove("fa-bars");
    } else {
        menuIcon.classList.remove("fa-times");
        menuIcon.classList.add("fa-bars");
    }
});

console.log("Hello World");