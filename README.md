# DeepFaceAuthentication
DeepFaceAuthentication is a multi-factor authentication (MFA) system that enhances security by using facial recognition as an additional layer of authentication. It leverages machine learning, computer vision, and liveness detection to ensure that only legitimate users can gain access, preventing spoofing attacks from photos or videos.

---

## 🚀 Key Features
✅ **Facial Recognition-Based MFA** – AI-powered authentication system.  
✅ **Liveness Detection** – Prevents spoofing using blinking and motion analysis.  
✅ **No Special Hardware Needed** – Works with standard 2D cameras.  
✅ **Fast & Secure Authentication** – Real-time identity verification.  
✅ **Flexible Deployment** – Works with APIs, mobile apps, or standalone applications.  

---

## 📂 Project Folder Structure

```bash
mfa-face-recognition/
│── 📂 backend/                # Backend logic
│    ├── 📂 models/            # Trained ML models (face recognition, liveness)
│    ├── 📂 services/          # Business logic (facial auth, token verification)
│    ├── 📂 database/          # Database models & queries (PostgreSQL/MongoDB)
│    ├── 📂 utils/             # Helper functions (logging, encryption)
│    ├── main.py               # Entry point for Streamlit UI
│
│── 📂 models/                 # Machine Learning models
│    ├── face_recognition.py   # Facial recognition logic
│    ├── liveness_detection.py # Anti-spoofing model
│    ├── train_model.py        # Model training script
│
│── 📂 scripts/                # Utility scripts
│    ├── preprocess_data.py    # Preprocess dataset for training
│    ├── test_face_recog.py    # Script to test facial recognition
│
│── 📂 config/                 # Configuration settings
│    ├── settings.py           # Environment variables, API keys
│    ├── database.py           # Database connection
│
│── 📂 tests/                  # Unit tests
│    ├── test_face_auth.py     # Test face authentication
│
│── 📂 docs/                   # Documentation
│    ├── README.md             # Project overview
│    ├── API_DOCS.md           # API documentation
│
│── Dockerfile                 # Containerization setup
│── requirements.txt            # Python dependencies
│── .gitignore                  # Ignore unnecessary files
│── README.md                   # Project description
```

---

## 🛠️ Tech Stack

- 🔹 **Python (OpenCV, Dlib, TensorFlow)** – Face detection & recognition  
- 🔹 **Streamlit** – Web-based UI for authentication  
- 🔹 **SQLite/PostgreSQL** – Securely store facial embeddings  
- 🔹 **FastAPI/Flask** – API integration for authentication  
- 🔹 **Docker** – Containerized deployment  

---

## ⚙️ Installation & Setup

Follow these steps to set up and run the project on your local machine:

### **1️⃣ Clone the Repository**
```bash
git clone [https://github.com/your-username/mfa-face-recognition.git](https://github.com/BVishal-Geek/DeepFaceAuthentication.git)
cd mfa-face-recognition
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Streamlit App**
```bash
streamlit run backend/main.py
```

---

## 📈 Future Enhancements

- 🔹 Integration with **Cloud MFA Providers** (AWS Cognito, Azure AD)  
- 🔹 **WebRTC-based Remote Authentication**  
- 🔹 **Iris & Voice Recognition** as Additional MFA Factors  

---

## 👨‍💻 Contributing

Contributions are welcome! Please submit a pull request with detailed explanations of the changes.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contact

For any questions or issues, please reach out to:  
📧 Email: vishal.bakshi@gwu.edu   
🌐 GitHub: [BVishal-Geek](https://github.com/BVishal-Geek)  
