import os

from flask import Flask, request
from Thaispoon import Spoonerism

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    return "R U LOST!!!"

# Create a GET /translate that accepts keyword arguments for the text and returns the spoonerism
@app.route("/translate")
def translate():
    """Return the spoonerism of the given text."""
    text = request.args.get("text", "")
    return Spoonerism(text).Loolang()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))