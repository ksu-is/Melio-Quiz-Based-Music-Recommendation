import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def load_songs():
    songs = []
    with open("melio_songs.csv", newline="", encoding="utf-8") as file:
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
    energy = request.form.get("energy")
    activity = request.form.get("activity")

    songs = load_songs()
    matches = []

    for song in songs:
        score = 0

        if song["mood"] == mood:
            score += 1

        song_genres = song["genre"].split(",")
        if genre in song_genres:
            score += 1

        if song["energy"] == energy:
            score += 1

        if song["activity"] == activity:
            score += 1

        if score > 0:
            song["score"] = score
            matches.append(song)

    matches.sort(key=lambda x: x["score"], reverse=True)

    top_matches = matches[:5]

    return render_template("results.html", songs=top_matches)

if __name__ == "__main__":
    app.run(debug=True)
