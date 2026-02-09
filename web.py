from flask import Flask;

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"""
    <b>AHOOOJ</b>
    <br />
    <img src="/static/img_vodka.jpg" alt="Vodka">
    """


if __name__ == "__main__":
    app.run(debug=True)
