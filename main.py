import pandas as pd
import pickle
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from pysentimiento import create_analyzer

app = FastAPI()

analyzer = create_analyzer(task="sentiment", lang="es")
df = pd.read_csv('db.csv')     
cv = pickle.load(open("count_vectorizer.pickle", "rb"))
RF = pickle.load(open("RF_nlp.pickle", "rb"))

class Pred(BaseModel):
    review: str

def feeling(review):
    output_sent = analyzer.predict(review).output
    if output_sent == 'POS':
        return 'positivo'
    elif output_sent == 'NEG':
        return 'negativo'
    else:
        return 'neutro'

@app.get("/")
async def read_item(n: int = 10):
    return df.loc[0:n-1].to_dict('records')

@app.post("/pred/")
async def create_item(pred: Pred):
    return {'review': pred.review, 'feeling': feeling(pred.review), 'score': str(RF.predict(cv.transform([pred.review]))[0])}