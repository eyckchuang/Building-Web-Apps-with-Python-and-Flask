from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import mongoengine as me
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydata'
mongo = PyMongo(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'mydata',
    'host': 'localhost',
    'port':27017
}
db_mongo = MongoEngine(app)


class Students(me.Document):
    name = me.StringField(required=True)
    course = me.StringField()
    gender = me.StringField()
    mobile = me.IntField()
    username = me.StringField(required=True, primary_key=True)
    password = me.StringField()


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    pwd = db.Column(db.String)
    name = db.Column(db.String)
    role = db.Column(db.String)
    dept = db.Column(db.String)
    salary = db.Column(db.Integer)

    def __init__(self, id, pwd, name, role, dept, salary):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.role = role
        self.dept = dept
        self.salary = salary


# class Students(db.Model):
#     name = db.Column(db.String(20))
#     course = db.Column(db.String(20))
#     gender = db.Column(db.String(10))
#     mobile = db.Column(db.Integer)
#     username = db.Column(db.String(6), primary_key=True)
#     password = db.Column(db.String(8), nullable=False)
#
#     def __init__(self, name, course, gender, mobile, username, password):
#         self.name = name
#         self.course = course
#         self.gender = gender
#         self.mobile = mobile
#         self.username = username
#         self.password = password


class Books(db.Model):
    bookID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    borrower = db.Column(db.String(6), db.ForeignKey('Students.username'))

    def __init__(self, id, title, author, borrower):
        self.id = id
        self.title = title
        self.author = author
        self.borrower = borrower
