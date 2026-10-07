// Elementos de la página
const mensaje = document.getElementById("mensaje");
const botones = document.querySelectorAll(".btn-prestamo");

// Se agrega un evento "click" a cada botón de préstamo
botones.forEach(function (boton) {
    boton.addEventListener("click", function () {
        // Fila del material seleccionado y sus datos
        const fila = boton.closest("tr");
        const titulo = fila.dataset.titulo;
        const dias = fila.dataset.dias;

        // Mensaje para el usuario
        mensaje.textContent =
            'Seleccionaste "' + titulo + '" para préstamo. ' +
            "Tienes " + dias + " días para devolverlo.";
        mensaje.classList.add("activo");

        // El material pasa a no estar disponible
        const estado = fila.querySelector(".estado");
        estado.textContent = "No disponible";
        estado.classList.remove("disponible");
        estado.classList.add("no-disponible");

        boton.textContent = "Prestado";
        boton.disabled = true;
    });
});