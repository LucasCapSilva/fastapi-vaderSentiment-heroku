from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    


app = FastAPI()


@app.get("/")
async def create_item():

    return {"mensagem":"hello word"}
