# FastAPI backend for VaakSetu (work in progress)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "VaakSetu backend is under construction"}
