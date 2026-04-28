import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def load_songs():
    songs = []
    with open("songs.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append(row)
    return songs
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/results", methods=["POST"])
def results():
    mood = request.form.get("mood")
    genre = request.form.get("genre")

    return render_template("results.html", mood=mood, genre=genre)

if __name__ == "__main__":
    app.run(debug=True)
