from flask import Flask, render_template, redirect, request, make_response
from database import News, Article
from enums import UpdateType
from user import User, actived_steam_users, steam_openid_url
from urllib.parse import urlencode

app = Flask(__name__)
News.start()

def render(html, with_auth: bool = False, **args):
	cookies = request.cookies
	user_id_exist = "user_id" in cookies
	user = None

	if user_id_exist:
		user_id = str(cookies.get("user_id"))

		user = User.get_user(user_id)

	print(user)
	if with_auth:
		if user:
			return render_template(html, user=user, **args)
		
		return redirect("/")
	
	return render_template(html, user=user, **args)

@app.route("/")
def main():
	return render("main.html")

@app.route("/gmod/loading")
def loading():
	return render("loading.html")

@app.route("/projects")
def projects():
	print(Article.is_exist("dbdabe91-18eb-11ee-9a44-2e3b706c43a1"))

	return render("projects.html")

@app.route("/news")
def news():
	available_news = News.get_news()

	return render("news.html", with_auth=False, news=available_news)

@app.route("/news/")
def news_redirect():
	return redirect("/news")

@app.route("/news/<uuid>")
def article(uuid):
	article_info = News.get_article(uuid)
	info = Article.get_info(uuid)
	if not info: 
		return redirect("/news")

	return render("article.html", with_auth=False, info_keys=len(info.keys()), info=info, update_type=UpdateType, article_info=article_info)

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

@app.route("/steam_auth")
def steam_auth():
	params = {
		'openid.ns': "http://specs.openid.net/auth/2.0",
		'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
		'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
		'openid.mode': 'checkid_setup',
		'openid.return_to': 'http://127.0.0.1:50000/auth_test',
		'openid.realm': 'http://127.0.0.1:50000'
	}
	
	query_string = urlencode(params)
	auth_url = steam_openid_url + "?" + query_string

	return redirect(auth_url)

@app.route("/auth_test")
def auth_test():
	print(request.args["openid.identity"])
	id = request.args["openid.identity"].split("/")[-1]

	uuid = User.create_user(id)

	response = make_response(redirect("/"))
	response.set_cookie("user_id", uuid)

	print("UUID")
	print(uuid)

	print("actived_steam_users")
	print(actived_steam_users)

	return response

@app.route("/donate")
def donate():
	return render("donate.html", with_auth=True)

if __name__ == "__main__":
	app.run(port=50000, debug=True)
