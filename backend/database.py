"""Simple SQLite database helpers."""

import sqlite3
from pathlib import Path
from typing import List

from .models import Task

DB_PATH = Path("database/assistant.db")


def init_db() -> None:
    """Create the tasks table if it doesn't exist."""
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            notes TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def add_task(task: Task) -> None:
    """Insert a task into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, due_date, notes) VALUES (?, ?, ?)",
        (task.title, task.due_date.isoformat() if task.due_date else None, task.notes),
    )
    conn.commit()
    conn.close()


def list_tasks() -> List[Task]:
    """Retrieve all tasks from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    rows = cursor.execute("SELECT title, due_date, notes FROM tasks").fetchall()
    conn.close()
    tasks = []
    for title, due, notes in rows:
        tasks.append(
            Task(title=title, due_date=due if due else None, notes=notes)
        )
    return tasks
