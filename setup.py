from setuptools import setup, find_packages

setup(
    name="mfa_face_recognition",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "onnxruntime",
        "fastapi",
        "uvicorn",
        "sqlite3",
        "cryptography",
        "python-jose"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)