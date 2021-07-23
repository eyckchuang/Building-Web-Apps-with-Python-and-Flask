from flask import Flask, url_for, redirect, abort
print (__name__)
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('hello'))
    url1=url_for('hello')
    url2=url_for('welcome')
    return "<a href={}>click here for hello()</a>".format(url1)+\
           "<br><a href={}>click here for welcome()</a>".format(url2)

@app.route('/hello/<name>')
def hello(name):
    # abort(401)
    return "Hello {}!".format(name)

def welcome():
    return 'Welcome to Flask Framework'

@app.route('/numbers/<int:a>/<float:b>')
def numbers(a, b):
    return "the numbers are {} anf {}".format(a,b)

app.add_url_rule('/hello/<name>', 'hello', hello)
app.add_url_rule('/welcome','welcome',welcome)
app.add_url_rule('/numbers/<int:a>/<float:b>','numbers',numbers)
