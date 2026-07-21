# 🔒 Secure User Data Vault

A secure cloud-based web application developed using **Flask** that demonstrates secure user authentication, password hashing, AES-256 encryption, and capability code authentication.

---

## 📌 Project Overview

The Secure User Data Vault allows users to:

- Register a secure account
- Generate a unique capability code
- Authenticate using email, password, and capability code
- Store sensitive information securely
- Encrypt confidential data using AES-256 (Fernet)
- Access decrypted information only after successful authentication

---

## 🚀 Features

- User Registration
- Secure Login
- Capability Code Authentication
- Password Hashing (bcrypt)
- AES-256 Encryption (Fernet)
- SHA-256 Capability Code Hashing
- SQLite Database
- Secure Dashboard
- Session-based Authentication

---

## 🛠 Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- bcrypt
- cryptography (Fernet)
- HTML5
- CSS3

---

## 📁 Project Structure

```
CA_CLOUD_COMPUTING_TASK_2/
│
├── models/
├── services/
├── static/
├── templates/
├── screenshots/
├── report/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/ag48665/CLOUD_COMPUTING_CODE_ALPHA_TASK_2.git
```

Navigate to the project folder:

```bash
cd CLOUD_COMPUTING_CODE_ALPHA_TASK_2
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🔐 Security Features

- Passwords are hashed using **bcrypt**.
- Sensitive information is encrypted using **AES-256 (Fernet)**.
- Capability codes are hashed using **SHA-256**.
- Secure session management.
- Protected dashboard access.
- SQLite secure data storage.

---

## 📸 Application Screenshots

- Figure 1 – Secure User Registration Interface
- Figure 2 – Successful Registration with Generated Capability Code
- Figure 3 – Secure Login Interface
- Figure 4 – Capability Code Authentication
- Figure 5 – Application Workflow
- Figure 6 – Secure Dashboard Displaying Decrypted User Information

---

## 🎯 Learning Outcomes

This project demonstrates:

- Cloud application development with Flask
- Secure authentication mechanisms
- Password hashing with bcrypt
- AES-256 encryption using Fernet
- Capability-based authentication
- Secure database management
- Web application security best practices

---

## 👩‍💻 Author

**Agata**

Cloud Computing Module

2026

---

## 📄 License

This project was developed for educational purposes as part of a Cloud Computing coursework assignment.