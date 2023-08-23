from fastapi.testclient import TestClient

from demo_poetry.calc_server import app


def test_client_1_add():
    client = TestClient(app)
    num = 3
    operator = "add"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    assert url == "http://localhost:8000/calculate/add?num=3"
    headers = {"user-id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 3


def test_client_1_subtract():
    client = TestClient(app)
    num = 4
    operator = "subtract"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -1


def test_client_1_multiply():
    client = TestClient(app)
    num = 4
    operator = "multiply"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -4


def test_client_1_divide():
    client = TestClient(app)
    num = -2
    operator = "divide"
    headers = {"user-id": "client1"}
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 2


def test_divide_by_zero():
    client = TestClient(app)
    num = 0
    operator = "divide"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 400


def test_clear():
    client = TestClient(app)
    operator = "clear"
    url = f"http://localhost:8000/calculate/{operator}"
    headers = {"user-id": "client1"}
    response = client.delete(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 0.0


def test_put_in():
    client = TestClient(app)
    num = -2
    operator = "put_in"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client1"}
    response = client.patch(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -2


client2 = TestClient(app)


def test_client_2_add():
    client2 = TestClient(app)
    num = 3
    operator = "add"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 3


def test_client_2_subtract():
    client2 = TestClient(app)
    num = 4
    operator = "subtract"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -1


def test_client_2_multiply():
    client2 = TestClient(app)
    num = 4
    operator = "multiply"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -4


def test_client_2_divide():
    client2 = TestClient(app)
    num = 4
    operator = "divide"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -1


def test_divide_by_zero_client2():
    client2 = TestClient(app)
    num = 0
    operator = "divide"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 400


def test_clear_client2():
    client2 = TestClient(app)
    operator = "clear"
    url = f"http://localhost:8000/calculate/{operator}"
    headers = {"user-id": "client2"}
    response = client2.delete(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 0.0


def test_put_in_clinet2():
    client2 = TestClient(app)
    num = 10
    operator = "put_in"
    url = f"http://localhost:8000/calculate/{operator}?num={num}"
    headers = {"user-id": "client2"}
    response = client2.patch(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 10


def test_client1_unchanged():
    client = TestClient(app)
    headers = {"user-id": "client1"}
    url = "http://localhost:8000/calculate/add?num=0"
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -2


##def test_users():
##response = client.get("http://localhost:8000/users")
##assert response.status_code == 200
##result = response.json()["result"]
##assert result == 2
