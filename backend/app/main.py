from fastapi import FastAPI

app = FastAPI(title="E-Réunion")


@app.get("/health")
def health():
    return {"status": "ok"}