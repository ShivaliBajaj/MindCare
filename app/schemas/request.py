from pydantic import BaseModel, Field, field_validator


class AnalysisRequest(BaseModel):
    """
    Request schema for behavioral text analysis.
    """

    text: str = Field(..., min_length=1, max_length=5000)

    @field_validator("text")
    @classmethod
    def text_must_not_be_blank(cls, value: str) -> str:
        """Reject input that contains only whitespace."""
        if not value.strip():
            raise ValueError("Text cannot be empty or whitespace-only.")
        return value
