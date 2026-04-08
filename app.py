from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import smtplib

app = Flask(__name__)
CORS(app)

# LOAD USERS
def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

# REGISTER
import pickle
app = Flask(__name__)
CORS(app)

# ✅ LOAD MODEL HERE
model = pickle.load(open("model.pkl", "rb"))
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    values = [[
        float(data["temperature"]),
        float(data["pressure"]),
        float(data["vibration"]),
        float(data["load"])
    ]]

    prediction = model.predict(values)

    if prediction[0] == 1:
        result = "⚠️ High Risk - Maintenance Required"
        send_email("jyothiprasad249@gmail.com", data, result)   # ✅ correct
    else:
        result = "✅ System Normal"

    return jsonify({"result": result})

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    print("Register Data:", data)  # Debug

    users = load_users()
    users.append(data)
    save_users(users)

    return jsonify({"message": "User registered successfully"})

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    users = load_users()

    for user in users:
        if user["username"] == data["username"] and user["password"] == data["password"]:
            return jsonify({"status": "success"})

    return jsonify({"status": "fail"})

# EMAIL FUNCTION
from email.mime.text import MIMEText
from datetime import datetime
def send_email(receiver_email, data, result):
    sender = "jp9829132@gmail.com"
    app_password = "jqkfzhqnxkiwpnvf"

    try:
        # 🕒 TIME-BASED GREETING
        hour = datetime.now().hour
        if hour < 12:
            greeting = "Good Morning"
        elif hour < 17:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        # 📊 MESSAGE CONTENT
        message = f"""
{greeting},

⚠️ Alert from AI Monitoring System

Sensor Details:
Temperature : {data['temperature']}
Pressure    : {data['pressure']}
Vibration   : {data['vibration']}
Load        : {data['load']}

Prediction Result:
{result}

Please take necessary action if required.

Regards,
AI Monitoring System
"""

        msg = MIMEText(message, "plain", "utf-8")
        msg["Subject"] = "🚨 AI System Alert"
        msg["From"] = sender
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, app_password)

        server.sendmail(sender, receiver_email, msg.as_string())
        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Error sending email:", e)
def send_reset_email(receiver_email, newpass):
    sender = "jp9829132@gmail.com"
    app_password = "jqkfzhqnxkiwpnvf"

    try:
        message = f"""
Password Reset Successful

Your new password is: {newpass}

Please login using your new password.

Regards,
AI Monitoring System
"""

        msg = MIMEText(message, "plain", "utf-8")
        msg["Subject"] = "Password Reset"
        msg["From"] = sender
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, app_password)

        server.sendmail(sender, receiver_email, msg.as_string())
        server.quit()

        print("✅ Reset email sent successfully")

    except Exception as e:
        print("❌ Error sending reset email:", e)        

# RESET PASSWORD
@app.route("/reset", methods=["POST"])
def reset():
    data = request.json

    # 🔒 Validate input
    if not data or "email" not in data or "newpass" not in data:
        return jsonify({"message": "Invalid input"}), 400

    users = load_users()

    for user in users:
        if user["email"] == data["email"]:
            user["password"] = data["newpass"]
            save_users(users)

            # 📧 Send reset email
            send_reset_email(data["email"], data["newpass"])

            return jsonify({"message": "Password reset & email sent"})

    return jsonify({"message": "Email not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)