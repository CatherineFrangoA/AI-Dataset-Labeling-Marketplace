function showMessage() {
    document.getElementById("message").innerHTML =
        "Welcome! Let's start labeling AI datasets.";
}

async function registerUser(event) {
    event.preventDefault();

    const fullname = document.getElementById("fullname").value;
    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                fullname: fullname,
                email: email,
                username: username,
                password: password
            })
        });

        const result = await response.json();

        if (response.ok) {
            alert("Registration successful!");
            window.location.href = "login.html";
        } else {
            alert(result.detail);
        }
    } catch (error) {
        alert("Cannot connect to backend");
    }
}

async function loginUser(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const result = await response.json();

        if (response.ok) {
            alert("Login successful!");
            window.location.href = "index.html";
        } else {
            alert(result.detail);
        }
    } catch (error) {
        alert("Cannot connect to backend");
    }
}