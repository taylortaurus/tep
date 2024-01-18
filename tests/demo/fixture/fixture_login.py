import pytest


@pytest.fixture(scope="session")
def login(HTTPRequestKeyword):
    def _function():
        url = "http://127.0.0.1:5000/login"
        headers = {"Content-Type": "application/json"}
        body = {"username": "dongfanger", "password": "123456"}
        response = HTTPRequestKeyword("post", url=url, headers=headers, json=body)
        assert response.status_code < 400
        return {"Content-Type": "application/json", "Cookie": f"{response.json()['Cookie']}"}

    return _function
