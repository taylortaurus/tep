def test(HTTPRequestKeyword):
    response = HTTPRequestKeyword("get", url="http://httpbin.org/status/200")
    assert response.status_code == 200
