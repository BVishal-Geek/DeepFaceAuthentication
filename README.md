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
│── 📂 mfa_face_recognition/   # Package directory (must have __init__.py)
│    ├── 📂 services/          # Facial authentication logic
│    │    ├── face_auth.py     # Verifies user identity
│    │    ├── liveness_check.py # (Optional) Detects spoofing
│    │    ├── token_manager.py # MFA token management
│    │
│    ├── 📂 database/          # Database logic
│    │    ├── db.py            # Database connection
│    │    ├── user_data.py     # Store, retrieve, and delete user embeddings
│    │
│    ├── 📂 utils/             # Helper functions
│    │    ├── image_processing.py # Preprocesses images
│    │    ├── logging_handler.py  # Custom logging
│    │    ├── encryption.py       # Encrypt embeddings
│    │
│    ├── 📂 models/            # Pretrained models
│    │    ├── face_model.onnx  
│    │    ├── liveness_model.onnx 
│    │
│    ├── 📂 scripts/           # Utility scripts
│    │    ├── capture_image.py      # Opens camera
│    │    ├── enroll_user.py        # Enrolls user
│    │    ├── redo_enrollment.py    # Deletes old data and re-enrolls user
│    │
│    ├── __init__.py           # Marks this as a Python package
│    ├── main.py               # API entry point (FastAPI/Flask)
│
│── 📂 tests/                  # Unit tests
│── setup.py                   # Packaging file for pip installation
│── pyproject.toml              # Alternative packaging method (modern way)
│── requirements.txt            # Dependencies list
│── README.md                   # Documentation
│── .gitignore                  # Ignore unnecessary files
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
