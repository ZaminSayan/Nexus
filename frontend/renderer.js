async function sendCommand(command) {
  try {
    const response = await fetch("http://localhost:5000/execute", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ command })
    });

    const data = await response.json();
    return data.message;

  } catch (error) {
    return "Backend not reachable.";
  }
}