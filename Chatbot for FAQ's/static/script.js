async function sendMessage() {

    const input =
        document.getElementById("userInput");

    const message =
        input.value.trim();

    if (message === "") return;

    const chatBox =
        document.getElementById("chatBox");

    chatBox.innerHTML +=
        `<div class="user">
            ${message}
        </div>`;

    input.value = "";

    const response =
        await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

    const data =
        await response.json();

    chatBox.innerHTML +=
        `<div class="bot">
            ${data.answer}
        </div>`;

    chatBox.scrollTop =
        chatBox.scrollHeight;
}