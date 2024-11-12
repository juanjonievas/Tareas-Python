// Espera a que el documento esté cargado
document.addEventListener("DOMContentLoaded", function() {
    // Selecciona el contenedor y la sección de contacto
    const body = document.body;
    const contacto = document.getElementById("contacto");
    
    // Añade un evento de clic al body para mostrar la sección de contacto
    body.addEventListener("click", function() {
        // Cambia la clase para mostrar la sección de contacto
        contacto.classList.remove("contacto-oculto");
        contacto.classList.add("contacto-visible");
    }, { once: true }); // Solo se ejecutará una vez
});




