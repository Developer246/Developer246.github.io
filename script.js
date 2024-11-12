document.getElementById("send-button").addEventListener("click", async () => {
    const inputField = document.getElementById("user-input");
    const userMessage = inputField.value;
    if (!userMessage) return;

    addMessageToChat(userMessage, "user");
    inputField.value = "";

    // Llamada a la API de OpenAI para obtener respuesta
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    });
    
    const data = await response.json();
    addMessageToChat(data.message, "bot");
});

function addMessageToChat(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageElem = document.createElement("div");
    messageElem.className = sender === "user" ? "user-message" : "bot-message";
    messageElem.innerText = message;
    chatBox.appendChild(messageElem);
    chatBox.scrollTop = chatBox.scrollHeight;
}
