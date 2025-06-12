# 📦  Chatbot

A full-stack chatbot-based product search application built with Flask and SQLite. It allows users to register, log in, search for products using natural queries, and reset passwords via email.

![Dashboard](screenshots/dashboard.png)

---

## 🚀 Features

- 🧑‍💻 User Signup/Login system
- 🔐 Secure password hashing with Flask-Login
- 📬 Password reset via email with secure token links
- 🛒 Chat-based product search (Books, Electronics, Textiles)
- 🧠 Natural language query matching using simple NLP logic
- 📷 Product cards with dynamic images
- ✅ Session-based authentication with protected routes
- 🗃️ SQLite as the backend database

---

## 🛠️ Technology Stack

**Backend**:
- Python 3.11
- Flask
- Flask-Login
- Flask-Mail
- Flask-CORS
- SQLAlchemy (ORM)
- SQLite3

**Frontend**:
- HTML5 + CSS3
- Vanilla JavaScript (for chat interactions)
- Jinja2 Templates (Flask rendering)

---

## 📂 Folder Structure

```
CHATBOT/
├── Backend/
│   ├── app.py                  # Main Flask app
│   ├── config.py               # Configs + .env loader
│   ├── .env                    # Secrets (ignored in Git)
│   ├── models/                 # DB models (User, Product)
│   ├── routes/                 # Chat routes
│   ├── auth/                   # Login/Signup/Forgot Password
│   ├── database/               # DB init script
│   ├── templates/              # HTML templates (Jinja2)
│   ├── static/                 # CSS and JS assets
├── frontend/                   # Optional separate JS interface
├── screenshots/                # 📸 UI screenshots
├── README.md                   # ✅ You're here
```

---

## 📽️ Demo Video

▶️ (https://github.com/user-attachments/assets/c9a09701-8131-405d-951b-ff4b665765bc)
---

## 📸 Screenshots

### 🔐 Signup & Login
![Image](https://github.com/user-attachments/assets/9bb944d0-1967-4161-97da-f3af9b5d3804)
![Image](https://github.com/user-attachments/assets/ebdda088-1376-459f-9145-e68ca39e4b98)

### 💬 Chat Interface
![Image](https://github.com/user-attachments/assets/edbd0fd9-9659-4f95-94f4-5591408db962)

### 🔍 Product Cards
![Image](https://github.com/user-attachments/assets/5300f564-c31e-4a73-8159-70fe3bd11c85)
![Image](https://github.com/user-attachments/assets/62049cad-2061-42aa-8483-242f417e8401)
![Image](https://github.com/user-attachments/assets/e0059e54-ec60-4496-a0d5-1947ccbd27c7)
![Image](https://github.com/user-attachments/assets/1477786c-e7bd-4aa7-b510-78f20bfb0f3b)

### 🔁 Forgot Password
![Image](https://github.com/user-attachments/assets/71ab1739-a54a-4e3b-8abd-6a0b5c32de6f)

---

## 🧪 How to Run Locally

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/CHATBOT.git
cd CHATBOT/Backend
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file:
```env
SECRET_KEY=your-secret-key
MAIL_USERNAME=yourname@gmail.com
MAIL_PASSWORD=your-app-password
```

### 5. Initialize the Database
```bash
python database/init_db.py
```

### 6. Run the App
```bash
python app.py
```

Visit: `http://localhost:5000/`

---

## 💬 Sample Queries

- "Books under 500"
- "Python"
- "Data science"
- "Show me electronics"
- "Affordable notebooks"

---

## 🛡️ Security Highlights

- Passwords stored securely using Werkzeug hashing
- Email-based password reset with secure token and 1-hour expiry
- Protected routes using `@login_required`
- `.env` file used for hiding sensitive data (SECRET_KEY, Mail creds)

---

## 📘 License
MIT License

---

## 👩‍💼 Author
**Bhavya Gupta** — Internship Case Study, June 2025

> Created as part of Uplyft Full Stack Internship Assignment

---

Need the 📘 project report or 📊 presentation? Let me know!
