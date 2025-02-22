let index = 0;
function showSlide(n) {
    let slides = document.querySelector(".slides");
    index += n;
    if (index < 0) index = slides.children.length - 1;
    if (index >= slides.children.length) index = 0;
    slides.style.transform = `translateX(${-index * 100}%)`;
}

function prevSlide() { showSlide(-1); }
function nextSlide() { showSlide(1); }
