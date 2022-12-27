from flask import Flask

my_app = Flask(__name__)

@my_app.route("/")
def hello():
	return "Hi, I am Kamal, how are you"


@my_app.route("/blog")
def my_blog():
	return "This is Kamal's blog"


