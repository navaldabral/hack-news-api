from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_top_news_max_limit():
    response = client.get("/top-news?count=100")  # return 100 stories
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 100  
    assert all("Title" in story for story in data)
    assert all("By" in story for story in data)
    assert all("URL" in story for story in data)

def test_get_top_news_default():
    response = client.get("/top-news")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10  
    assert all("Title" in story for story in data)
    assert all("By" in story for story in data)
    assert all("URL" in story for story in data)

def test_get_top_news_with_count():
    response = client.get("/top-news?count=5")  # return 5 stories
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5  
    assert all("Title" in story for story in data)
    assert all("By" in story for story in data)
    assert all("URL" in story for story in data)

def test_get_top_news_invalid_count():
    response = client.get("/top-news?count=0")
    assert response.status_code == 422  # Validation error due to invalid 'count'


