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
  $(document).on("click", ".close-button", function() {
    // Удаляем модальное окно
    $(this).closest(".my-modal").remove();
  });

  // При нажатии на фон модального окна
  $(document).on("click", ".my-modal", function(event) {
    // Проверяем, был ли клик на самом фоне модального окна, а не на изображении или кнопке закрытия
    if ($(event.target).hasClass("my-modal")) {
      // Удаляем модальное окно
      $(this).remove();
    }
  });
});
