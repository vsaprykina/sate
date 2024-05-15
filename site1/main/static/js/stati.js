document.addEventListener("DOMContentLoaded", function() {
    const showMoreButton = document.getElementById("showMoreButton");
    const hiddenArticles = document.querySelector(".hiddenArticles");

    showMoreButton.addEventListener("click", function() {
      hiddenArticles.style.display = "grid"; // Показываем скрытые статьи при нажатии на кнопку
      showMoreButton.style.display = "none"; // Скрываем кнопку после нажатия
    });
  });
