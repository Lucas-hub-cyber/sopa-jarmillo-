from fastapi import FastAPI

app = FastAPI(title="Bot Guardián Jaramillo")

@app.get("/")
def home():
    return {"status": "Bot Guardián Jaramillo activo 🚀"}
