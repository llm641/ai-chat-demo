async function sendMessage() {

    const message =
        document.getElementById("message").value;

    const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
            method: "POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                text: message
            })
        }
    );

    const data = await response.json();

    document.getElementById(
        "reply"
    ).innerText = data.reply;
}