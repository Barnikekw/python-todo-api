from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Saját Junior Projekt API", version="1.0")

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

fake_db: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Szia! A backend szerver fut."}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return fake_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    for t in fake_db:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Ilyen ID-val már létezik feladat.")
    fake_db.append(task)
    return task