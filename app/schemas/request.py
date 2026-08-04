from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    """
    Request schema for behavioral text analysis.
    """

    text: str