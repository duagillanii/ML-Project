# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a person is at **high risk** or **low risk** of heart disease using Machine Learning. It compares multiple classification algorithms and selects the best-performing model based on evaluation metrics such as Accuracy, Precision, Recall, and F1-Score.

The project also allows users to enter their own health information and receive a heart disease risk prediction.

---

## 🎯 Objectives

- Predict the likelihood of heart disease using patient health data.
- Compare the performance of multiple Machine Learning models.
- Select the best-performing model.
- Save the trained model for future predictions.
- Provide an easy-to-use prediction interface.

---

## 📂 Dataset

The project uses the **Heart Disease Dataset** containing medical attributes such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- Slope of ST Segment
- Number of Major Vessels (CA)
- Thalassemia
- Target (Heart Disease Condition)

---

## 🛠 Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Random Forest Classifier
- Multi-Layer Perceptron (Neural Network)

The best-performing model is automatically selected based on the highest **F1-Score**.

---

## 📊 Model Evaluation

Each model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics help compare the performance of different classification algorithms.

---

## ⚙️ Project Workflow

1. Load the Heart Disease dataset.
2. Explore and visualize the data.
3. Separate features and target variable.
4. Standardize the dataset using StandardScaler.
5. Split the data into training and testing sets.
6. Train multiple Machine Learning models.
7. Evaluate model performance.
8. Select the best-performing model.
9. Save the trained model and scaler using Joblib.
10. Predict heart disease risk from user input.

---

## 📥 User Input Features

The prediction system accepts the following inputs:

| Feature | Description |
|----------|-------------|
| Age | Age in years |
| Sex | Male = 1, Female = 0 |
| Chest Pain Type | 0–3 |
| Resting Blood Pressure | mm Hg |
| Cholesterol | mg/dl |
| Fasting Blood Sugar | >120 mg/dl |
| Resting ECG | 0–2 |
| Maximum Heart Rate | bpm |
| Exercise-Induced Angina | Yes/No |
| Oldpeak | ST Depression |
| Slope | ST Segment Slope |
| CA | Number of Major Vessels |
| Thal | Thalassemia Type |

---

## 📈 Output

The system predicts one of the following:

- ✅ Low Risk of Heart Disease
- ❤️ High Risk of Heart Disease

---

## 📁 Project Structure

```
Heart-Disease-Prediction/
│
├── heart.csv.csv
├── best_heart_model.joblib
├── scaler.joblib
├── Heart_Disease_Prediction.ipynb
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Open the notebook in Google Colab or Jupyter Notebook.

4. Run all cells.

5. Enter the requested patient information.

6. View the prediction.

---

## 📷 Sample Prediction

```
Prediction Complete

The model predicts:

HIGH RISK of Heart Disease
```

or

```
Prediction Complete

The model predicts:

LOW RISK of Heart Disease
```

---

## 📌 Future Improvements

- Develop a web application using Flask or Streamlit.
- Deploy the model online.
- Add support for larger healthcare datasets.
- Improve prediction accuracy through hyperparameter tuning.
- Include explainable AI (XAI) techniques for prediction interpretation.

---

## 👨‍💻 Author

**Syeda Dua**

Computer Science Student

Machine Learning & Data Analytics Enthusiast

---

## 📄 License

This project is intended for educational and research purposes.
