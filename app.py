
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    fahrenheit = None
    kelvin = None

    if request.method == "POST":
        try:
            celsius = float(request.form["celsius"])
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
        except ValueError:
            pass

    return render_template("index.html", fahrenheit=fahrenheit, kelvin=kelvin)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




