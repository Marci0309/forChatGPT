"""Pydantic models for API requests and responses."""

from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    """Represents a single task item."""

    title: str
    due_date: Optional[datetime] = None
    notes: Optional[str] = None
