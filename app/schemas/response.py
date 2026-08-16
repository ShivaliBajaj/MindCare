"""Pydantic schemas for MindCare API responses."""

from typing import Literal

from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    """Successful response from the behavioral text
    analysis endpoint"""
    
    status: Literal["success"]
    received_text: str
    message: str