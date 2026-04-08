### AI Agent for Smart Infrastructure Monitoring and Predictive Maintenance

### Project Overview
This project is an AI-powered system designed to monitor infrastructure systems such as machines, utilities, and industrial equipment. It uses Machine Learning to predict potential failures before they occur, enabling proactive maintenance and reducing downtime.

### The system includes:
- Frontend dashboard for user interaction
- Backend API using Flask
- Machine Learning model for prediction
- Email alert system for real-time notifications

### Objectives
- Develop an intelligent AI-based monitoring system
- Predict system failures using machine learning
- Provide real-time alerts through email
- Reduce maintenance costs and downtime
- Improve efficiency and reliability of infrastructure systems

### Features
- User Authentication (Login / Register / Forgot Password)
- Real-time Data Input (Temperature, Pressure, Vibration, Load)
- AI Prediction System
- Email Alerts for High Risk Conditions
- Password Reset via Email
- Interactive UI Dashboard

### Tech Stack
### Frontend:
- HTML
- CSS
- JavaScript

### Backend:
- Python
- Flask
- Flask-CORS

### Machine Learning:
- Scikit-learn
- Pandas
- NumPy

### Email Service:
- SMTP (Gmail App Password)

## Project Structure
IBM/
│
├── app.py # Flask backend
├── model.pkl # Trained ML model
├── users.json # User database
│
├── static/
│ ├── style.css # Styling
│ └── script.js # Frontend logic
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── forgot.html
│ └── dashboard.html
│
└── README.md

## How to Run the Project

### 1️. Clone the Repository
### 2️. Install Dependencies
pip install flask flask-cors numpy pandas scikit-learn
### 3️. Run the Application
python app.py
## 4️. Open in Browser
http://127.0.0.1:5000/
## Sample Inputs
### Normal Condition:
Temperature: 45
Pressure: 20
Vibration: 2
Load: 40
### High Risk Condition:
Temperature: 90
Pressure: 50
Vibration: 8
Load: 85
## Email Configuration

## To enable email alerts:

Enable 2-Step Verification in Gmail
Generate App Password
Update in app.py:
sender = "your_email@gmail.com"
app_password = "your_16_digit_app_password"
## SDG Alignment

This project supports Sustainable Development Goal 9 (Industry, Innovation, and Infrastructure) by promoting smart monitoring, automation, and predictive maintenance.

## Expected Outcomes
- Reduced system failures and downtime
- Improved efficiency in infrastructure monitoring
- Cost-effective maintenance strategy
- Scalable AI-based solution
  ##  Project Screenshots

### Login Page
![Login](Screenshot%202026-04-08%20215204.png)

### Dashboard
![Dashboard](Screenshot%202026-04-08%20220846.png)

### Prediction Result
![Result](Screenshot%202026-04-08%20221000.png)
  ## Security Note
- Passwords are currently stored in plain text (for learning purpose)
- In real-world applications, password hashing should be implemented
## Author

Name: Jyothi Prasad
Course: B.Tech CSE
Institution: Chadalawada Ramanamma Engineering College

## Contact

Email: jyothiprasad249@gmail.com

## Acknowledgment

This project is developed as part of the IBM Internship Program focusing on AI and real-world problem solving.
