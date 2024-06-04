function toggleMenu() {
  var navMenu = document.getElementById("nav-menu");
  navMenu.classList.toggle("show");
}

document.addEventListener("click", function(event) {
  var navMenu = document.getElementById("nav-menu");
  var menuToggle = document.querySelector(".menu-toggle");
  var closeButton = document.querySelector(".close-button");

  if (
    !navMenu.contains(event.target) &&
    event.target !== menuToggle &&
    event.target !== closeButton
  ) {
    navMenu.classList.remove("show");
  }
});