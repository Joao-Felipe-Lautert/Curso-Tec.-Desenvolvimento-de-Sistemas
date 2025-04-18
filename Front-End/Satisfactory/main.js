let indice = 0;

function mudarSlide(direcao) {
    const slides = document.querySelectorAll(".slide");
    const totalSlides = slides.length;
    indice += direcao;

    if (indice < 0) {
        indice = totalSlides -1;
    } else if (indice >= totalSlides) {
        indice = 0;
    }

    document.querySelector(".carousel-container").style.transform = `translateX(${-indice * 400}px)`;
}
