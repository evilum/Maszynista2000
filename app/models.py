from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    incorrect_answers = db.relationship('IncorrectAnswer', backref='user', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
    options = db.Column(db.JSON, nullable=False)
    image = db.Column(db.String(150), nullable=True)
    category = db.Column(db.String(150), nullable=False)

class IncorrectAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    answer = db.Column(db.String(1), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
