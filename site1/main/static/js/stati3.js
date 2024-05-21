document.addEventListener("DOMContentLoaded", function() {
    const showMoreButton = document.getElementById("showMoreButton");
    const hideButton = document.getElementById("hideButton");
    const articles = document.querySelectorAll(".other-articles .article");

    // Скрываем все статьи, кроме первых 4
    for (let i = 4; i < articles.length; i++) {
      articles[i].style.display = "none";
    }

    showMoreButton.addEventListener("click", function() {
      // Показываем все скрытые статьи при нажатии на кнопку
      for (let i = 4; i < articles.length; i++) {
        articles[i].style.display = "grid";
      }
      showMoreButton.style.display = "none"; // Скрываем кнопку "Показать еще"
      hideButton.style.display = "block"; // Показываем кнопку "Скрыть"
    });

    hideButton.addEventListener("click", function() {
      // Скрываем все статьи, кроме первых 4, при нажатии на кнопку "Скрыть"
      for (let i = 4; i < articles.length; i++) {
        articles[i].style.display = "none";
      }
      showMoreButton.style.display = "block"; // Показываем кнопку "Показать еще"
      hideButton.style.display = "none"; // Скрываем кнопку "Скрыть"
    });
});