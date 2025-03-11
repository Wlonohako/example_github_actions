from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


test_app = TestClient(app)


def test_root():
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}