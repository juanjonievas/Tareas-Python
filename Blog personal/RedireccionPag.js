function mostrarVideo() {
    // Obtener elementos
    const contenido = document.querySelector('.contenido');
    const fin = document.getElementById('fin');
    const blogTitle = document.querySelector('.titulo-principal');
    const videoContainer = document.getElementById('video-container');
    const video = document.getElementById('video');

    // Ocultar otros elementos
    if (contenido) contenido.classList.add('hidden');
    if (fin) fin.classList.add('hidden');
    if (blogTitle) blogTitle.classList.add('hidden');

    // Mostrar el contenedor del video
    if (videoContainer) videoContainer.style.display = 'block';

    // Reproducir el video y redirigir cuando termine
    if (video) {
        video.play();
        video.onended = function() {
            window.location.href = 'pagina1.html'; // Cambia a la página principal que desees
        };
    } else {
        console.error("El elemento de video no se encontró");
    }
}
