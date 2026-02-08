import requests

# URL BoozeAPI (verejné API s drinkami)
url = "https://api.sampleapis.com/cocktails/drinks"

# Pošleme HTTP GET požiadavku
response = requests.get(url)

# Skontrolujeme, či bola požiadavka úspešná
if response.status_code == 200:
    drinks = response.json()

    vodka_count = 0
    gin_count = 0
    rum_count = 0

    # Prejdeme všetky drinky
    for drink in drinks:
        ingredients = drink.get("ingredients", [])

        # Pre istotu premeníme ingrediencie na malé písmená
        ingredients_lower = [i.lower() for i in ingredients]

        if "vodka" in ingredients_lower:
            vodka_count += 1
        if "gin" in ingredients_lower:
            gin_count += 1
        if "rum" in ingredients_lower:
            rum_count += 1

    print("Počet drinkov s vodkou:", vodka_count)
    print("Počet drinkov s ginom:", gin_count)
    print("Počet drinkov s rumom:", rum_count)

else:
    print("Chyba pri načítaní dát z API")
