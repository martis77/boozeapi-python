import requests

# URL pre jednotlivé alkoholy
vodka_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Vodka"
gin_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Gin"
rum_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Rum"

def count_drinks(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        drinks = data.get("drinks")
        return len(drinks) if drinks else 0
    else:
        return 0

vodka_count = count_drinks(vodka_url)
gin_count = count_drinks(gin_url)
rum_count = count_drinks(rum_url)

print("Počet drinkov s vodkou:", vodka_count)
print("Počet drinkov s ginom:", gin_count)
print("Počet drinkov s rumom:", rum_count)
