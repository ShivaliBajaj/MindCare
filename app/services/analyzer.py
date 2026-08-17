from app.schemas.response import AnalysisResponse

def analyze_text(text: str) -> AnalysisResponse:
    """
    Placeholder analysis service.

    Future responsibilities:
    - MentalBERT inference
    - Behavioral signal extraction
    - Severity estimation
    - Explainable AI outputs
    """

    clean_text = text.strip()

    if not clean_text:
        return AnalysisResponse(
            status="error",
            message="Input text cannot be empty."
        )

    response = AnalysisResponse(
        status="success",
        received_text=clean_text,
        message="Analysis pipeline placeholder"
    )

    return response
