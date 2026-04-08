from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# load model
saved_data = pickle.load(open("../models/credit_risk_model.pkl","rb"))

model = saved_data["model"]
feature_names = saved_data["features"]

@app.get("/")
def home():
    return {"message":"SmartCredit API running"}

@app.post("/predict")
def predict(age:int, loan_amount:int, duration:int, income_ratio:int):

    data = pd.DataFrame({col:[0] for col in feature_names})

    data["age"] = age
    data["credit_amount"] = loan_amount
    data["month_duration"] = duration
    data["payment_to_income_ratio"] = income_ratio

    probability = model.predict_proba(data)[0][1]

    risk_score = probability * 100

    credit_score = int(850 - risk_score * 5.5)

    return {
        "default_probability": probability,
        "risk_score": risk_score,
        "credit_score": credit_score
    }