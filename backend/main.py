from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="AcadMate AI Backend")


class Question(BaseModel):
    subject: str
    question: str


@app.get("/")
def home():
    return {
        "message": "AcadMate AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


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

    # Split the file into sections
    sections = content.split("------------------------------------------------")

    # Extract keywords from the user's question
    keywords = data.question.lower().split()

    answer = "Topic not found in syllabus."

    # Skip the first section because it contains the subject and topic list
    for section in sections[1:]:

        section = section.strip()

        if not section:
            continue

        lines = section.splitlines()

        if not lines:
            continue

        # First non-empty line is treated as the heading
        heading = lines[0].strip().lower()

        if any(keyword == heading or keyword in heading for keyword in keywords):
            answer = section
            break

    return {
        "status": "success",
        "subject": data.subject,
        "question": data.question,
        "answer": answer
    }