from flask import request

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/results", methods=["POST"])
def results():
    mood = request.form.get("mood")
    genre = request.form.get("genre")

    return f"You selected {mood} and {genre}"
