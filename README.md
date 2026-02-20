# 🐶 Dog Breed Detection using Deep Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)

---

## 📌 Project Overview

Dog Breed Detection is a Deep Learning-based image classification web application that predicts the breed of a dog from an uploaded image.

This project uses Transfer Learning (VGG19) with TensorFlow and is deployed using Flask for real-time predictions.

---

## 🚀 Features

- Upload dog image
- Automatic image preprocessing
- Breed prediction using trained CNN model
- Real-time result display
- Simple web interface

---

## 🧠 Model Architecture

- Pre-trained Model: VGG19 (ImageNet weights)
- Base layers frozen
- Custom Dense layers added
- Softmax output layer
- Optimizer: Adam
- Loss: Categorical Crossentropy

---

## 🏗 Technical Architecture

User → Flask App → Image Preprocessing → VGG19 Model → Prediction Output

---

## 📁 Project Structure

DOG_BREED_PREDICTION/

├── static/  
├── templates/  
│   ├── index.html  
│   ├── predict.html  
│   └── output.html  
├── uploads/  
├── dogbreed.h5  
├── train_model.py  
├── app.py  
└── README.md  

---

## 📊 Dataset

The dataset contains categorized dog breed images stored in separate folders.

Example breeds:
- Labrador
- Golden Retriever
- German Shepherd
- Pug
- Bulldog
- Beagle

All images are resized to 224x224 before training.

---

## ⚙️ Installation

### Clone Repository

git clone https://github.com/your-username/DOG_BREED_PREDICTION.git  
cd DOG_BREED_PREDICTION  

### Install Dependencies

pip install tensorflow flask numpy pillow  

---

## ▶️ Run the Application

python app.py  

Open browser and go to:

http://127.0.0.1:5000/

---

## 📈 Training the Model (Optional)

python train_model.py  

This will generate:

dogbreed.h5  

---

## 🖥 How It Works

1. User uploads a dog image  
2. Image is resized and normalized  
3. Image is passed to VGG19 model  
4. Model predicts dog breed  
5. Result displayed on webpage  

---

## 🎯 Future Improvements

- Add more dog breeds  
- Add prediction confidence score  
- Improve UI design  
- Deploy on cloud  
- Add webcam-based detection  

---

## 👨‍💻 Technologies Used

- Python  
- TensorFlow  
- Keras  
- Flask  
- HTML  
- CSS  

---

## 📜 License

This project is for educational purposes.
