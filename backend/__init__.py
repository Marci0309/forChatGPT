"""Application factory and route registration for FastAPI."""

from fastapi import FastAPI

from .routes import router
from .database import init_db

app = FastAPI(title="Student Assistant API")

# Initialize the SQLite database on startup
@app.on_event("startup")
def on_startup():
    init_db()

# Register API routes
app.include_router(router)
