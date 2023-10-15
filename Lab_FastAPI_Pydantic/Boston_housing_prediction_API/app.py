from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import xgboost
class features(BaseModel):
    CRIM:float
    ZN:float
    INDUS:float
    CHAS:int
    NOX:float
    RM:float
    AGE:float
    DIS:float
    RAD:int
    TAX:float
    PTRATIO:float
    B:float
    LSTAT:float

app = FastAPI()

model = pickle.load(open('C:/Users/21261/Desktop/Master 2/Devops and MLops/Project/model_boston.pkl','rb'))

@app.get('/')
def home():
    return {'ML model for Boston House prices prediction'}

@app.post('/Prices_predictions')
async def Prices_predictions(features : features):
    pred = model.predict([[features.CRIM,features.ZN,
                           features.INDUS,features.CHAS,features.NOX,
                           features.RM,features.AGE,features.DIS,features.RAD,features.TAX,features.PTRATIO,features.B,
                           features.LSTAT]])
    return ({"Prediction is : ":str(pred[0])})

if __name__ == '__main__':
    uvicorn.run("app:app",host="0.0.0.0",port=8080,reload=True)