import requests

url = "http://127.0.0.1:5000/api/add_bloedvoorraden"

data = {
    "Bloedzakje_ID": "17",
    "Bloedgroep": "B+",
    "Volume": 4282000,
    "Verzamelingsdatum": "2023-05-01",
    "Vervaldatum": "2023-02-03"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
