from fastapi import FastAPI, HTTPException, Depends
from .core.config import settings
from pydantic import BaseModel
from typing import Annotated
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
models.Base.metadata.create_all(bind=engine)

class ProjectBase(BaseModel):
    name: str

@app.get("/")
def root():
    return {"hello": "world"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/projects", response_model=list[ProjectBase])
async def list_projects(db:db_dependency):
    result = db.query(models.Projects).all()
    if not result:
        raise HTTPException(status_code=404, detail=f'Projects not found')
    return result

@app.post("/projects")
async def create_projects(project: ProjectBase, db:db_dependency):
    db_project = models.Projects(name=project.name)
    db.add(db_project)
    db.commit()
