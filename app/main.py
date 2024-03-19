from fastapi import FastAPI, HTTPException, Depends, Response
from pydantic import BaseModel, field_validator
from pydantic_geojson import FeatureModel
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import date

from .core.config import settings
from .database import engine, SessionLocal
from . import models

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
models.Base.metadata.create_all(bind=engine)

class ProjectBase(BaseModel):
    name: str
    description: str = None
    area_of_interest: FeatureModel
    start_date: date
    end_date: date

    @field_validator('end_date')
    def validate_end_date(cls, value: date, values) -> date:
        start_date = values.data.get('start_date')
        if value <= start_date:
            raise ValueError("End date must be greater than the start date.")
        return value

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/projects", response_model=list[ProjectBase])
async def list_projects(db: db_dependency):
    result = db.query(models.Projects).all()
    return result

@app.get("/projects/{project_id}", response_model=ProjectBase)
async def read_project(project_id: int, db: db_dependency):
    result = db.query(models.Projects).filter(models.Projects.id==project_id).first()
    if not result:
        raise HTTPException(status_code=404, detail=f'Project not found')
    return result

@app.post("/projects", response_model=ProjectBase)
async def create_project(project: ProjectBase, db: db_dependency):
    result = models.Projects(**project.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

@app.put("/projects/{project_id}", response_model=ProjectBase)
async def update_project(project_id: int, project: ProjectBase, db: db_dependency):
    result = db.query(models.Projects).filter(models.Projects.id==project_id)
    if not result:
        raise HTTPException(status_code=404, detail=f'Project not found')
    result.update(project.dict(), synchronize_session=False)
    db.commit()

    return result.first()

@app.delete("/projects/{project_id}")
async def delete_project(project_id: int, db: db_dependency):
    result = db.query(models.Projects).filter(models.Projects.id==project_id)
    if not result:
        raise HTTPException(status_code=404, detail='Project not found')

    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=204)
