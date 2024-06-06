$(document).ready(function() {
  // При нажатии на изображение в галерее
  $(".gallery3 img").click(function() {
    // Получаем атрибут src изображения
    var imgSrc = $(this).attr("src");
    // Создаем новый элемент <img> для отображения увеличенной версии изображения
    var modalImg = $("<img>").attr("src", imgSrc).addClass("modal-image");
    // Создаем кнопку закрытия модального окна
    var closeButton = $("<span>").addClass("close-button").html("&times;");
    // Создаем блок для модального окна и добавляем в него изображение и кнопку закрытия
    var myModal = $("<div>").addClass("my-modal").append(modalImg, closeButton);
    // Добавляем модальное окно в body
    $("body").append(myModal);
  });

  // При нажатии на кнопку закрытия модального окна
  $(document).on("click", ".close-button", function(event) {
    // Останавливаем распространение события, чтобы предотвратить срабатывание события "click" на модальном окне
    event.stopPropagation();
    // Удаляем модальное окно при клике
    $(this).closest(".my-modal").remove();
  });

  // При нажатии на модальное окно
  $(document).on("click", ".my-modal", function() {
    // Удаляем модальное окно при клике
    $(this).remove();
  });
});