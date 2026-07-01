from fastapi import FastAPI

app = FastAPI(
    title="AI Powered Hospital Management System",
    version = "1.0.0"
)
@app.get("/")
def root():
    return {
        "message" : "Welcome to AI Powered Hospital Management System"
    }