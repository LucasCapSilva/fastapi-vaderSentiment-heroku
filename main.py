  
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

class Item(BaseModel):
    mensagem: str
    
app = FastAPI()

@app.get("/")
async def create_item():
    return {"mensagem":"hello word"}

@app.post("/analysy")
async def create_item(item: Item):
    score = analyser.polarity_scores(item.mensagem) # avaliação de polaridade de sentimento da mensagem
    compound = (analyser.polarity_scores(item.mensagem)['compound'])  # capitura da média do sentimento da mensagem
    if compound > 0:
      mensagemSentimento = "noticia positiva" 
    elif compound >= 0:
      mensagemSentimento = "noticia neutra" 
    else:
      mensagemSentimento = "noticia negativa"
    return {"mensagem":item.mensagem,"sentimento":mensagemSentimento}