from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import re

app = FastAPI(
    title="AcadMate AI Backend",
    version="1.0.0",
    description="Offline AI Tutor using syllabus text files"
)


# -----------------------------
# Request Model
# -----------------------------
class Question(BaseModel):
    subject: str
    question: str


# -----------------------------
# Home API
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "AcadMate AI Backend Running 🚀"
    }


# -----------------------------
# Health Check API
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "OK"
    }


# -----------------------------
# Ask Question API
# -----------------------------
@app.post("/ask")
def ask(data: Question):

    # Subject file
    file_path = f"data/{data.subject.lower()}.txt"

    # Check subject file exists
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Subject not found."
        )

    # Read subject file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Split into sections
    sections = content.split("------------------------------------------------")

    # Extract clean keywords
    keywords = re.findall(r"\b\w+\b", data.question.lower())

    answer = "Topic not found in syllabus."

    # Skip first section
    for section in sections[1:]:

        section = section.strip()

        if not section:
            continue

        lines = section.splitlines()

        if not lines:
            continue

        heading = lines[0].strip().lower()

        # Search keywords in heading
        if any(keyword in heading for keyword in keywords):
            answer = section
            break

    return {
        "status": "success",
        "subject": data.subject,
        "question": data.question,
        "answer": answer
    }