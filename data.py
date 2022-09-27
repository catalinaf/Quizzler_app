import requests

URL = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}

api_response = requests.get(URL, params=PARAMETERS)
api_response.raise_for_status()

data = api_response.json()
question_data = data["results"]
