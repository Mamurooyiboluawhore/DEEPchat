#!/usr/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    userName = db.Column(db.String(150), nullable=False, unique=True)
    userMail = db.Column(db.String(150), nullable=False, unique=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    photo =db.Column(db.String(23), nullable=False, default="default.jpg")
    db.relationship('ToDo', backref='user', lazy=True)
    
    def __repr__(self):
        return f"User('{self.userName}', '{self.userMail}', '{self.create_at}', '{self.photo}')"

class ToDo(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(150), nullable=False)
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"ToDo('{self.content}', '{self.createdAt}')" 

@app.route("/")
@app.route("/home")
def Home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

