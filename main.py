from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World and Universe 2"}