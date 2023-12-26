from flask import Flask, request, redirect, url_for, render_template, session
from weather import main as get_weather
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback_secret_key')



@app.route("/", methods=["GET", "POST"])
def index():
    card1 = get_weather("Istanbul")
    card2 = get_weather("Paris")
    card3 = get_weather("Rome")
    card4 = get_weather("New York")
    card5 = get_weather("Edinburgh")
    card6 = get_weather("Ankara")

    city = None
    data = None

    if request.method == "POST":
        city = request.form["cityName"]
        data = get_weather(city)
        session['data'] = data
        session['city'] = city
        return redirect(url_for("index"))

    data = session.pop('data', None)
    city = session.pop('city', None)

    return render_template(
        "index.html",
        city=city,
        data=data,
        card1=card1,
        card2=card2,
        card3=card3,
        card4=card4,
        card5=card5,
        card6=card6
    )

if __name__ == "__main__":
    app.run(debug=True)