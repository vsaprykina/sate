// Объявляем переменные в начале
let prevButton, nextButton, slideIndex = 0;

// Получаем кнопки "Prev" и "Next"
prevButton = document.querySelector('.prev');
nextButton = document.querySelector('.next');

// Добавляем обработчики событий
prevButton.addEventListener('click', () => {
  plusSlides(-1);
});

nextButton.addEventListener('click', () => {
  plusSlides(1);
});

showSlides();

function plusSlides(n) {
  slideIndex += n;
  showSlides();
}

function showSlides() {
  let slides = document.getElementsByClassName("testimonial-slide");
  if (slideIndex >= slides.length) {
    slideIndex = 0;
  } else if (slideIndex < 0) {
    slideIndex = slides.length - 1;
  }

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  
  slides[slideIndex].style.display = "block";
}