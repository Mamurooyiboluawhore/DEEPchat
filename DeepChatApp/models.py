from DeepChatApp import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(150), nullable=False, unique=True)
    userMail = db.Column(db.String(150), nullable=False, unique=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    photo =db.Column(db.String(23), nullable=False, default="default.jpg")
    db.relationship('Todo', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.userName}', '{self.userMail}', '{self.create_at}', '{self.photo}')"

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), nullable=False)
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Todo('{self.content}', '{self.createdAt}')"
