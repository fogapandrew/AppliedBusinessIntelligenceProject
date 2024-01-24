// static/script.js
function makeApiRequest() {
    const form = document.getElementById("apiForm");
    const formData = new FormData(form);
    const url = "http://127.0.0.1:5000/api/add_bloedvoorraden";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(Object.fromEntries(formData)),
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById("response");

        if (data.message) {
            // Display success message
            responseDiv.innerHTML = `<p style="color: green;">${data.message}</p>`;
        } else {
            // Display error message
            responseDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("response").innerHTML = "Error occurred. Check the console for details.";
    });
}
