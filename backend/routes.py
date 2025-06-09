"""API routes for managing tasks."""

from fastapi import APIRouter
from typing import List

from .models import Task
from .database import add_task, list_tasks

router = APIRouter()

@router.post("/tasks", response_model=Task)
def create_task(task: Task) -> Task:
    """Store a new task and return it."""
    add_task(task)
    return task

@router.get("/tasks", response_model=List[Task])
def get_tasks() -> List[Task]:
    """Return all stored tasks."""
    return list_tasks()
