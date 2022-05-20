import pandas as pd
import pickle
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from pysentimiento import create_analyzer

app = FastAPI()

class Pred(BaseModel):
    review: str

def feeling(review):
    analyzer = create_analyzer(task="sentiment", lang="es")
    output_sent = analyzer.predict(review).output
    if output_sent == 'POS':
        return 'positivo'
    elif output_sent == 'NEG':
        return 'negativo'
    else:
        return 'neutro'

@app.get("/")
async def read_item(n: int = 10):
    df = pd.read_csv('db_reviews_claro_feelings.csv')     
    return df.loc[0:n-1].to_dict('records')

@app.post("/pred/")
async def create_item(pred: Pred):
    cv = pickle.load(open("count_vectorizer.pickle", "rb"))
    RF = pickle.load(open("RF_nlp.pickle", "rb"))
    return {'review': pred.review, 'feeling': feeling(pred.review), 'score': str(RF.predict(cv.transform([pred.review]))[0])}