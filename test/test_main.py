from fastapi.testclient import TestClient
from app.main import app, get_db

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import pytest

client = TestClient(app)

# @pytest.fixture
# def override_get_db():
#     engine = create_engine('postgresql://geo_projects_test:geo_projects_test@localhost:5432/geo_projects_test')
#     TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#     try:
#         yield TestingSessionLocal()
#     finally:
#         TestingSessionLocal().close()

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}

# def test_list_projects():
#     response = client.get("/projects")
#     assert response.status_code == 200
#     assert response.json() == []

# def test_create_project():
#     project_data = {"name": "Test Project"}
#     response = client.post("/projects", json=project_data)
#     assert response.status_code == 200

# def test_create_project_invalid_data():
#     project_data = {"invalid_key": "Invalid Value"}
#     response = client.post("/projects", json=project_data)
#     assert response.status_code == 422

