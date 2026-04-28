from flask import Flask, render_template, request

app = Flask(__name__)

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
