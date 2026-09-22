# 🧠 OncOMind — Brain Cancer Prediction

> A deep-learning powered web application for classifying brain tumor MRI scans into four categories: **Glioma**, **Meningioma**, **No Tumor**, and **Pituitary**.

---

## 📌 Overview

OncOMind uses a Convolutional Neural Network (CNN) trained on MRI brain scan images to predict the type of brain tumor with high accuracy. It is served as a Flask web application where users can upload an MRI image and get an instant prediction.

---

## 🗂️ Project Structure

```
oncomind/
├── main.py                  # Flask web server
├── train.py                 # Model training script
├── requirements.txt         # Python dependencies
├── models/
│   └── model.h5             # Trained CNN model (Git LFS)
├── templates/
│   └── index.html           # Frontend UI
├── output/                  # App demo screenshots
└── uploads/                 # Runtime: uploaded MRI images (gitignored)
```

---

## 🧬 Dataset

The model is trained on the **Brain Tumor MRI Dataset** from Kaggle.

📥 **Download here:** [https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

After downloading, place it in this structure:
```
Brain_Tumor_Data/
├── Training/
│   ├── glioma/
│   ├── meningioma/
│   ├── notumor/
│   └── pituitary/
└── Testing/
    ├── 1/
    ├── 2/
    ├── 3/
    └── 4/
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sup18github/oncomind---Brain-Cancer-Prediction.git
cd oncomind---Brain-Cancer-Prediction
```

### 2. Install Git LFS (for the model file)

```bash
git lfs install
git lfs pull
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the web app

```bash
python main.py
```

Open your browser at [http://localhost:5000](http://localhost:5000)

---

## 🏋️ Training the Model

If you want to retrain from scratch, download the dataset first (see above), then:

```bash
python train.py
```

The best model checkpoint will be saved to `models/best_model.h5` and the final model to `models/final_model.h5`.

---

## 🧪 Model Architecture

| Layer | Details |
|-------|---------|
| Input | 128×128×3 |
| Conv2D | 32 filters, 3×3, ReLU |
| MaxPooling | 2×2 |
| Conv2D | 64 filters, 3×3, ReLU |
| MaxPooling | 2×2 |
| Conv2D | 128 filters, 3×3, ReLU |
| MaxPooling | 2×2 |
| Flatten | — |
| Dense | 512 units, ReLU |
| Dropout | 0.5 |
| Output | 4 units, Softmax |

**Optimizer:** Adam | **Loss:** Categorical Cross-Entropy

---

## 🏷️ Tumor Classes

| Label | Description |
|-------|-------------|
| `glioma` | Tumor originating from glial cells |
| `meningioma` | Tumor from the meninges (brain lining) |
| `notumor` | No tumor detected |
| `pituitary` | Tumor on the pituitary gland |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, TensorFlow/Keras
- **Frontend:** HTML, CSS, JavaScript
- **ML:** CNN (Convolutional Neural Network)
- **Model Storage:** Git LFS

---

## 📸 Screenshots

| Upload Screen | Prediction Result |
|---|---|
| ![Upload](output/Screenshot%202025-05-13%20222457.png) | ![Result](output/Screenshot%202025-05-13%20222732.png) |

---

## 📄 License

This project is open source. Feel free to fork, modify, and build upon it for research and educational purposes.
