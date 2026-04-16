from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import os

app = FastAPI()

# ✅ Load model safely (relative path)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR,"models/credit_risk_model.pkl")

saved_data = pickle.load(open("/Users/taniakhalid/SmartCredit/models/credit_risk_model.pkl", "rb"))
model = saved_data["model"]
features = saved_data["features"]

# ✅ Input schema (clean & structured)
class LoanInput(BaseModel):
    age: int
    credit_amount: int
    month_duration: int
    payment_to_income_ratio: int

@app.get("/")
def home():
    return {"message": "SmartCredit API running"}

@app.post("/predict")
def predict(data: LoanInput):

    # Create input dataframe
    df = pd.DataFrame([{col: 0 for col in features}])

    df["age"] = data.age
    df["credit_amount"] = data.credit_amount
    df["month_duration"] = data.month_duration
    df["payment_to_income_ratio"] = data.payment_to_income_ratio

    # Prediction
    prob = model.predict_proba(df)[0][1]

    risk_score = prob * 100
    credit_score = int(850 - risk_score * 5.5)

    return {
        "probability": prob,
        "risk_score": risk_score,
        "credit_score": credit_score
    }
