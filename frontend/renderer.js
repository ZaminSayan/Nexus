// renderer.js
const chat = document.getElementById("chat");
const inputField = document.getElementById("commandInput");

async function sendCommand(command) {
  try {
    const response = await fetch("http://127.0.0.1:5000/command", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command })
    });
    const data = await response.json();
    return data.response;
  } catch (error) {
    return "Backend not reachable.";
  }
}

function addMessage(sender, text) {
  const message = document.createElement("div");
  message.classList.add("message", sender);
  message.innerText = text;
  chat.appendChild(message);
  chat.scrollTop = chat.scrollHeight;
}

async function runCommand() {
  const input = inputField.value.trim();
  if (!input) return;

  addMessage("user", input);
  inputField.value = "";
  inputField.focus();

  const typing = document.createElement("div");
  typing.classList.add("message", "nexus", "typing");
  typing.innerText = "Nexus is thinking...";
  chat.appendChild(typing);
  chat.scrollTop = chat.scrollHeight;

  const responseText = await sendCommand(input);
  await new Promise(r => setTimeout(r, 800 + Math.random() * 700));

  typing.remove();
  addMessage("nexus", responseText);
}
const typing = document.createElement("div");
typing.classList.add("message", "nexus", "typing");
typing.innerHTML = "Nexus is thinking <span></span><span></span><span></span>";
chat.appendChild(typing);
chat.scrollTop = chat.scrollHeight;

inputField.addEventListener("keydown", (e) => {
  if (e.key === "Enter") runCommand();
});

window.onload = () => inputField.focus();