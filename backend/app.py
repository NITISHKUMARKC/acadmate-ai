from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import re

# ==========================================
# FastAPI Application
# ==========================================

app = FastAPI(
    title="AcadMate AI Backend",
    version="1.0.0",
    description="Offline AI Tutor using syllabus text files"
)

# ==========================================
# CORS Configuration
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Request Model
# ==========================================

class Question(BaseModel):
    subject: str
    question: str

# ==========================================
# Home API
# ==========================================

@app.get("/")
def home():
    return {
        "message": "AcadMate AI Backend Running 🚀"
    }

# ==========================================
# Health Check API
# ==========================================

@app.get("/health")
def health():
    return {
        "status": "OK"
    }

# ==========================================
# Ask Question API
# ==========================================

@app.post("/ask")
def ask(data: Question):

    file_path = f"data/{data.subject.lower()}.txt"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Subject not found."
        )

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    sections = content.split("------------------------------------------------")

    keywords = re.findall(r"\b\w+\b", data.question.lower())

    answer = "Topic not found in syllabus."

    for section in sections[1:]:

        section = section.strip()

        if not section:
            continue

        lines = section.splitlines()

        if not lines:
            continue

        heading = lines[0].strip().lower()

        if any(keyword in heading for keyword in keywords):
            answer = section
            break

    return {
        "status": "success",
        "subject": data.subject,
        "question": data.question,
        "answer": answer
    }