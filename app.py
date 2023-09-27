from flask import Flask, render_template, redirect
from database import News, Article
from enums import UpdateType


app = Flask(__name__)

News.start()

@app.route("/")
def main():
	return render_template("main.html")

@app.route("/gmod/loading")
def loading():
	return render_template("loading.html")

@app.route("/projects")
def projects():
	print(Article.is_exist("dbdabe91-18eb-11ee-9a44-2e3b706c43a1"))

	return render_template("projects.html")

@app.route("/news")
def news():
	available_news = News.get_news()

	return render_template("news.html", news=available_news)

@app.route("/news/")
def news_redirect():
	return redirect("/news")

@app.route("/news/<uuid>")
def article(uuid):
	article_info = News.get_article(uuid)
	info = Article.get_info(uuid)
	if not info: 
		return redirect("/news")

	return render_template("article.html", info_keys=len(info.keys()), info=info, update_type=UpdateType, article_info=article_info)

@app.route("/add/news/<title>")
def add_news(title):
	News.add_new(title, "img/placeholder.png")

	return redirect("/news")

@app.route("/add/article")
def add_info():
	# Article.add_update("9343dd98199311ee922e2e3b706c43a1", UpdateType.FEATURES.value, "Improve map!")
	# Article.add_update("9343dd98199311ee922e2e3b706c43a1", UpdateType.IMPROVEMENTS.value, "Delete bugs!")
	# Article.add_update("9343dd98199311ee922e2e3b706c43a1", UpdateType.FIXED.value, "Fix bugs!")

	return ""

@app.route("/donate")
def donate():
	return render_template("donate.html")

if __name__ == "__main__":
	app.run(port=50000, debug=True)
