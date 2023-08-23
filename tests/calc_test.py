from fastapi.testclient import TestClient

from demo_poetry.calc_server import app

client = TestClient(app)
operator = "none"
num = 0
url = f"http://localhost:8000/calculate/{operator}?num={num}"


def test_client_1_add():
    headers = {"user_id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 3


def test_client_1_subtract():
    headers = {"user_id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -1


def test_client_1_multiply():
    headers = {"user_id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -4


def test_client_1_divide():
    headers = {"user_id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 2


def test_divide_by_zero():
    headers = {"user_id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 2


def test_clear():
    headers = {"user_id": "client1"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 0.0


def test_put_in():
    headers = {"user_id": "client1"}
    response = client.patch(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 1000


client2 = TestClient(app)


def test_client_2_add():
    headers = {"user_id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 3


def test_client_2_subtract():
    headers = {"user_id": "client2"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -1


def test_client_2_multiply():
    headers = {"user_id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == -4


def test_client_2_divide():
    headers = {"user_id": "client1"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 2


def test_divide_by_zero_client2():
    headers = {"user_id": "client2"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 2


def test_clear_client2():
    headers = {"user_id": "client1"}
    response = client2.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 0.0


def test_put_in_clinet2():
    headers = {"user_id": "client1"}
    response = client.patch(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 10


def test_client1_unchanged():
    headers = {"user_id": "client"}
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 1000


def test_users():
    response = client.get("http://localhost:8000/users")
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == 2
