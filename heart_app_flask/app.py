from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("best_heart_model.joblib")
scaler = joblib.load("scaler.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Get data from form
            data = [
                float(request.form["age"]),
                int(request.form["sex"]),
                int(request.form["cp"]),
                float(request.form["trestbps"]),
                float(request.form["chol"]),
                int(request.form["fbs"]),
                int(request.form["restecg"]),
                float(request.form["thalach"]),
                int(request.form["exang"]),
                float(request.form["oldpeak"]),
                int(request.form["slope"]),
                int(request.form["ca"]),
                int(request.form["thal"])
            ]

            # Scale and predict
            input_data = np.array([data])
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)[0]

            if prediction == 1:
                result = "🚨 HIGH RISK of Heart Disease"
            else:
                result = "✅ LOW RISK of Heart Disease"

        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
