document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.getElementById("formularioSocio");

  formulario.addEventListener("submit", async function (e) {
    e.preventDefault();

    const datos = Object.fromEntries(new FormData(formulario).entries());

    try {
      const respuesta = await fetch("/registrar-socio", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(datos)
      });

      const resultado = await respuesta.json();

      if (resultado.exito) {
        alert("✅ Socio registrado correctamente.");
        formulario.reset();
      } else {
        alert("❌ Error: " + resultado.error);
      }
    } catch (error) {
      console.error("Error al conectar con el servidor:", error);
      alert("❌ No se pudo conectar con el servidor.");
    }
  });
});
