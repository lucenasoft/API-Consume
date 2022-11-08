import json

import requests


def buscar_dados():
    res = requests.get('https://api.adviceslip.com/advice')
    todo = json.loads(res.content)
    print(todo['slip']['advice'])


buscar_dados()
