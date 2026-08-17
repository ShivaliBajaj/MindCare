"""Pydantic schemas for MindCare API responses."""

from enum import Enum

from typing import Literal

from pydantic import BaseModel

class ReviewPriority(str, Enum):
    """Human-review priority; not a clinical diagnosis or treatment directive."""

    NOT_ASSESSED = "not_assessed"
    HUMAN_REVIEW_RECOMMENDED = "human_review_recommended"
    URGENT_HUMAN_REVIEW = "urgent_human_review"

class AnalysisResponse(BaseModel):
    """Successful response from the behavioral text
    analysis endpoint"""
    
    status: Literal["success"]
    analysis_status: Literal["placeholder"] = "placeholder"
    review_priority: ReviewPriority = ReviewPriority.NOT_ASSESSED
    received_text: str
    message: str