function toggleChat() {
            let chatContainer = document.getElementById("chatContainer");
            chatContainer.style.display = (chatContainer.style.display == "none" || chatContainer.style.display == "") ? "block" : "none";
        }

        function sendMessage() {
            let userInput = document.getElementById("userInput").value;

            if (!userInput.trim()) return;

            document.getElementById("chatBox").innerHTML += "<p class='user'>Você: " + userInput + "</p>";
            document.getElementById("userInput").value = "";

            fetch("/get_response", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userInput })
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById("chatBox").innerHTML += "<p class='bot'>Tony Stark: " + data.response + "</p>";
                    document.getElementById("chatBox").scrollTop = document.getElementById("chatBox").scrollHeight;
                });
        }
        function checkEnter(event) {
            if (event.key === "Enter") {
                sendMessage();  // Chama a função de envio quando o Enter é pressionado
            }
        }

        document.getElementById("userInput").addEventListener("keydown", checkEnter);