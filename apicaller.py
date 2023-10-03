import requests


class ApiCaller:
    def __init__(self, longurl):
        self.longurl = longurl

    def get_short_url(self):
        path = f"http://localhost:8000/short-changed/create/{self.longurl}"
        response = requests.get(path)
        data = response.json()
        short_url = data["shorturl"]
        return short_url

