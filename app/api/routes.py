from fastapi import APIRouter

from app.schemas.request import AnalysisRequest
from app.services.analyzer import analyze_text

router = APIRouter()


@router.post("/analyze")
def analyze(request: AnalysisRequest):
    return analyze_text(request.text)