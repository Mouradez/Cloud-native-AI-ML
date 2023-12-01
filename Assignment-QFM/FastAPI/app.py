import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

model = pickle.load(open('C:/Users/21261/Desktop/Assignement_MLops/Dep_Flask/classifier_svm.pkl','rb'))

app = FastAPI()

class Features(BaseModel):
    Gender: float
    Age: float
    Major: float
    Year: float
    CGPA:  float
    Marriage: float
    Anxiety: float
    Panic: float
    Treatment: float

@app.get("/")
def home():
    return {'Student Mental health prediction'}

@app.post("/predictions")
async def predictions(features : Features):
    features = [[features.Gender,features.Age,features.Major,features.Year,features.CGPA,
                features.Marriage,features.Anxiety,features.Panic,features.Treatment]]
    pred = model.predict(features)

    if pred[0]==0:
        pred = 'No, you dont have depression'
    else:
        pred = 'Yes, yo have depression'
    return {'prediction : ':pred}

if __name__ == '__main__':
    uvicorn.run("app:app", host="localhost", port=8080, reload=True)