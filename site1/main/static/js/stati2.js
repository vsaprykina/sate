document.addEventListener("DOMContentLoaded", function() {
    const showMoreButton = document.getElementById("showMoreButton");
    const hideButton = document.getElementById("hideButton");
    const hiddenArticles = document.querySelector(".hiddenArticles");

    showMoreButton.addEventListener("click", function() {
      hiddenArticles.style.display = "grid"; // Показываем скрытые статьи при нажатии на кнопку
      showMoreButton.style.display = "none"; // Скрываем кнопку "Показать еще"
      hideButton.style.display = "block"; // Показываем кнопку "Скрыть"
    });

    hideButton.addEventListener("click", function() {
      hiddenArticles.style.display = "none"; // Скрываем скрытые статьи при нажатии на кнопку "Скрыть"
      showMoreButton.style.display = "block"; // Показываем кнопку "Показать еще"
      hideButton.style.display = "none"; // Скрываем кнопку "Скрыть"
    });
});
