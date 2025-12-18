from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"URL Shortner is running"}
