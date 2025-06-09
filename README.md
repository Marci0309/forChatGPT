# AI-Powered Personal Assistant for Students

This repository contains a summer AI project focused on building a personal assistant for students. The assistant aims to help manage academic tasks, study efficiently, and boost productivity using modern NLP and recommendation techniques.

## Project Overview

This project aims to create an intelligent and user-friendly AI assistant, designed specifically to help students manage academic tasks, study efficiently, and boost productivity using advanced Natural Language Processing (NLP) and recommendation techniques.

## Key Features and Goals

### 1. Task and Deadline Management

* Automatically categorize and prioritize tasks.
* Natural language task interpretation and intelligent deadline reminders.

### 2. Intelligent Study Scheduler

* Analyze student productivity patterns.
* Recommend optimized study schedules based on historical data.

### 3. Personalized Resource Recommendations

* Suggest relevant educational materials (videos, articles, notes) tailored to each student’s learning style and subject preferences.

### 4. User-friendly Interface

* Develop a responsive and intuitive front-end interface using React.js, ensuring ease of use.

## Tech Stack

* **Backend**: Python, NLP models (spaCy, transformers), Flask or FastAPI.
* **Database**: SQL (e.g., PostgreSQL, SQLite) for structured storage.
* **Frontend**: React.js, focusing on clean and intuitive UX/UI.

## Backend Data and Structure

The backend stores **tasks** with the following fields:

- `title` – short description of the assignment or activity.
- `due_date` – optional deadline in ISO format.
- `notes` – any additional remarks.

The `backend/` folder now contains:

- `app.py` – entry point running the FastAPI server.
- `__init__.py` – application factory and route registration.
- `models.py` – Pydantic data models.
- `routes.py` – API endpoints for creating and retrieving tasks.
- `database.py` – simple SQLite helpers.
- `nlp_task_parser.py` – example script that parses a natural-language task description.

### Setup and Running the API

Install the required Python packages:

```bash
pip install fastapi uvicorn spacy python-dateutil
python -m spacy download en_core_web_sm
```

Launch the server with:

```bash
python -m backend.app
```

## Project Milestones (Sub-Goals)

* [ ] **Setup Project Environment and Repository**
* [ ] **Data Collection and Initial Dataset Creation**
* [ ] **Implement NLP-based Task Parsing**
* [ ] **Develop Task Prioritization Logic**
* [ ] **Build Recommendation and Scheduling Algorithms**
* [ ] **Create Backend API Endpoints**
* [ ] **Design and Implement Frontend UI**
* [ ] **Testing, Feedback Integration, and Optimization**

## Future Enhancements (Optional)

* Integration with external calendar apps (Google Calendar, Outlook).
* Incorporation of sentiment analysis to better understand student needs.
* Mobile application extension (iOS/Android).

