// NAVIGATION
function goToRegister() {
    window.location.href = "register.html";
}
function goToForgot() {
    window.location.href = "forgot.html";
}

// REGISTER
async function register() {
    const username = document.getElementById("reg_user").value.trim();
    const password = document.getElementById("reg_pass").value.trim();
    const email = document.getElementById("reg_email").value.trim();

    const msg = document.getElementById("msg");

    // EMPTY CHECK
    if (!username || !password || !email) {
        msg.innerText = "All fields are required";
        return;
    }

    // EMAIL VALIDATION
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        msg.innerText = "Enter valid email address";
        return;
    }

    // PASSWORD LENGTH
    if (password.length < 4) {
        msg.innerText = "Password must be at least 4 characters";
        return;
    }

    const res = await fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password, email })
    });

    const data = await res.json();

    msg.innerText = "Registered Successfully!";
    msg.style.color = "lightgreen";

    setTimeout(() => {
        window.location.href = "login.html";
    }, 1500);
}

// LOGIN
async function login() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const msg = document.getElementById("msg");

    if (!username || !password) {
        msg.innerText = "Please fill all fields";
        return;
    }

    const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password })
    });

    const result = await res.json();

    if (result.status === "success") {
        window.location.href = "dashboard.html";
    } else {
        msg.innerText = "Invalid username or password";
    }
}

// RESET PASSWORD
async function resetPassword() {
    const email = document.getElementById("email").value.trim();
    const newpass = document.getElementById("newpass").value.trim();
    const msg = document.getElementById("msg");

    if (!email || !newpass) {
        msg.innerText = "All fields are required";
        return;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        msg.innerText = "Enter valid email";
        return;
    }

    const res = await fetch("http://127.0.0.1:5000/reset", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, newpass })
    });

    const result = await res.json();
    msg.innerText = result.message;
}

// PREDICTION FUNCTION
async function predict() {
    const data = {
        temperature: Number(document.getElementById("temp").value),
        pressure: Number(document.getElementById("pressure").value),
        vibration: Number(document.getElementById("vibration").value),
        load: Number(document.getElementById("load").value)
    };

    const res = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await res.json();
    document.getElementById("output").innerText = result.result;
}