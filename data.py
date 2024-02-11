import requests

BASE_URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=BASE_URL, params=parameters).json()
question_data = response["results"]
