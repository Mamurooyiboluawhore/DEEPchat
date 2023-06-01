from flask import render_template
from DeepChatApp import app
from DeepChatApp.models import User, Todo

@app.route('/')
def Home():
        return render_template("index.html")
