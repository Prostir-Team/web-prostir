from flask import Flask, render_template, redirect
from database import News

app = Flask(__name__)

db_news = News()



@app.route("/")
def main():
	return render_template("main.html")

@app.route("/gmod/loading")
def loading():
	return render_template("loading.html")

@app.route("/projects")
def projects():
	return render_template("projects.html")

@app.route("/news")
def news():
	available_news = db_news.get_news()

	return render_template("news.html", news=available_news)

@app.route("/news/")
def news_redirect():
	return redirect("/news")

@app.route("/news/<id>")
def article(id):

	return render_template("article.html")

if __name__ == "__main__":
	app.run(port=50000, debug=True)
