import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(self.url)
        response.raise_for_status()  
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        json_data = json.loads(response_body)
        return json_data
        pass