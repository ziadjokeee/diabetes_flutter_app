from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_diabetes

app = FastAPI(title="Diabetes Prediction API")

class InputData(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

@app.post("/predict")
def predict(data: InputData):
    result = predict_diabetes([
        data.age, data.sex, data.bmi, data.bp,
        data.s1, data.s2, data.s3, data.s4,
        data.s5, data.s6
    ])
    return {"prediction": result}
