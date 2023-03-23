from flask import Flask, render_template
from valve.source.a2s import ServerQuerier
from valve.source.messages import PlayerEntry

app = Flask(__name__)
server = ServerQuerier(("91.203.5.123", 25016), 5)

@app.route("/")
def main():
	playersInfo = server.players()
	players = []

	for player in playersInfo["players"]:
		if player["name"] == "": continue
		
		players.append(player["name"])

	return render_template("main.html", players=players)

@app.route("/gmod/loading")
def loading():
	return render_template("loading.html")

@app.route("/projects")
def projects():
	return render_template("projects.html")

@app.route("/news")
def news():
	return render_template("news.html")

if __name__ == "__main__":
	app.run(port=50000, debug=True)
