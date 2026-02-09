import requests

response = requests.get(
    "https://boozeapi.com/api/v1/cocktails"
)


if response.status_code == 200:
    data = response.json()
    
    print("Success")

    print(len(data['data']))
    
    for drink in data['data']:
        print(drink["name"])

else:
    print("Error:", response.status_code, response.text)
