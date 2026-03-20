from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hola, soy Fatima Mohammed" in response.data or b"Hola, soy F\xc3\xa1tima Mohammed" in response.data
