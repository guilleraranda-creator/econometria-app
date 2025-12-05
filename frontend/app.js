// Lógica base de la app
function enviarNumero(numero) {
    fetch("https://econometria-app.onrender.com/square", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ number: numero })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Resultado recibido del backend:", data);
        alert("El resultado es: " + data.result);
    })
    .catch(error => {
        console.error("Error al conectar con backend:", error);
    });
}
