from fastapi import FastAPI

app = FastAPI()

VERSION = "0.1.0"

@app.get("/health")
def health_check():
    return {"status": "ok", "version": VERSION}