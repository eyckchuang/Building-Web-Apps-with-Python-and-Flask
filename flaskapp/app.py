import sqlite3

from flask import Flask, render_template, request, make_response

from flaskapp.encryption import encpwd

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/createtable')
def createtable():
    con = sqlite3.connect("mydata.db")
    cur = con.cursor()
    createqry = '''
    create table if not exists Students (
    Name string (20) not null,
    Course string (20) ,
    Gender string (20),
    Mobile integer (10),
    Username string (6) primary key not null,
    Password text (8) not null
    );
    '''
    cur.execute(createqry)
    return 'ok'


@app.route('/home')
def home():
    return render_template('home.html')


# @app.route('/')
# def index():
#     list=[5,8,4,6,7]
#     string='Hello'
#     return render_template('hh.html',list=list,string=string)

# def result():
#     students = [('Anil',55),('Rajeev',40),('Leela',60),('Zuber',75),('John',30)]
#     return render_template("langs.html",students=students)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nm = request.form.get('name')
        # nm = request.args.get('name')
        # nm = request.args.get('name')
        # nm = request.args.get('name')
        return """<b>Name:</b>{}<br>""".format(nm)

    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/hello/<name>/<int:age>')
def hello(name, age):
    return render_template('hello.html', name=name, age=age)


@app.template_filter("isodd")
def isodd(x):
    if x % 2 == 1:
        result = True
    else:
        result = False
    return result


@app.route('/<name>')
def index(name):
    return render_template('btn.html', name=name)


@app.route('/page')
def page():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('page.html', name=name, age=age)


@app.route('/form')
def form():
    return render_template('register.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template('setcookie.html'))
        resp.set_cookie('userID', user)
        return resp


@app.route('/readcookie')
def readcookie():
    name = request.cookies.get('userID')
    return render_template('readcookie.html', name=name)


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        con = sqlite3.connect("mydata.db")
        cur = con.cursor()
        msg = ''
        try:
            nm = request.form['name']
            gndr = request.form['gender']
            course = request.form['course']
            mob = request.form['mobile']
            usr = request.form['user']
            pw = request.form['pwd']
            ins = "insert into Students values(?,?,?,?,?,?)"
            cur.execute(ins, (nm, gndr, course, mob, usr, encpwd(pw)))
            con.commit()
            msg = "record successfully added"
        except Exception as e:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template('result.html', msg=msg)


@app.route('/list')
def list():
    con = sqlite3.connect("mydata.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Students;")
    students = cur.fetchall()
    return render_template("studentlist.html", students=students)


if __name__ == '__main__':
    app.run()
