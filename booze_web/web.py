from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://boozeapi.com/api/v1/cocktails"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # BoozeAPI balí drinky do kľúča 'data'
            vysledok = response.json()
            drinky = vysledok.get('data', []) 
        else:
            drinky = []
    except:
        drinky = []
    
    return render_template("index.html", vsetky_drinky=drinky)

if __name__ == "__main__":
    app.run(debug=True)