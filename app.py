from flask import Flask, render_template, request

app = Flask(__name__)

votes = {"Spring": 0, "Summer": 0, "Fall": 0, "Winter": 0}
season = "Spring"  # Default season (could be dynamic based on user vote)

@app.route("/", methods=["GET", "POST"])
def index():
    global season
    if request.method == "POST":
        vote = request.form.get("vote")
        if vote in votes:
            votes[vote] += 1
            season = vote.lower()  # Set season to the vote
    return render_template("index.html", votes=votes, season=season)

if __name__ == "__main__":
    app.run(debug=True)
