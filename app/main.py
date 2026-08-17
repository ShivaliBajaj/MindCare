from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="MindCare API",
    description=(
        "An early-stage suicide-risk intelligence system for decision support. "
        "MindCare does not provide diagnosis or treatment recommendations."
    ),
    version="0.1.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "MindCare backend is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}