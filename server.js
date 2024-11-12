const express = require("express");
const fetch = require("node-fetch");
const app = express();
const PORT = process.env.PORT || 3000;

// Reemplaza con tu clave de API de OpenAI
const OPENAI_API_KEY = "tu_clave_api";

app.use(express.json());
app.use(express.static("public"));

app.post("/chat", async (req, res) => {
    const { message } = req.body;

    const response = await fetch("https://api.openai.com/v1/engines/gpt-4/completions", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${OPENAI_API_KEY}`
        },
        body: JSON.stringify({
            model: "gpt-4",
            messages: [{ role: "user", content: message }]
        })
    });

    const data = await response.json();
    res.json({ message: data.choices[0].message.content });
});

app.listen(PORT, () => {
    console.log(`Servidor en ejecución en http://localhost:${PORT}`);
});
