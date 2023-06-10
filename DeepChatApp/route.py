from flask import render_template
from DeepChatApp import app
from DeepChatApp.models import User, Todo


@app.route('/landingP')
def landingP():
	return render_template("landP.html")
@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/registeration')
def registeration():
	return render_template("registeration")
	
@app.route('/')
def Home():
        return render_template("index.html")

@app.route('/main')
def about():
	return render_template("about.html")
