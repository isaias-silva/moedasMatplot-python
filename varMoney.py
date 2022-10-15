
import requests
import json

def variacao(dias,moeda):
    url = "https://economia.awesomeapi.com.br/json/daily/"+moeda+"-BRL/"+dias
    print(url)
    req = requests.get(url)
    data = json.loads(req.content)
    variacao = []
    for value in data:
        number = float(value["low"])
        variacao.append(round(number, 3))
    return list(reversed(variacao))