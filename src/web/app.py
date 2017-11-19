from flask import Flask, render_template, request, session, abort, flash, redirect, url_for
from sqlalchemy.orm import sessionmaker
from tabledef import *
import os
engine = create_engine('sqlite:///labeler.db', echo=True)
DATA_PATH = "/Users/mneary1/Desktop/data/"
app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect("/menu")
 
@app.route('/login', methods=['GET'])
def show_login():
	return render_template("login.html")

@app.route('/login', methods=['POST'])
def do_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()

    if result:
        session['logged_in'] = True
        session['username'] = result.username
    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    del session['username']
    return redirect("/")

@app.route('/menu')
def menu():

	if not session.get("username"):
		flash("You're not logged in!")
		return redirect("/login")

	Session = sessionmaker(bind=engine)
	s = Session()

	current_user = session['username']
	lines_marked = s.query(Line).filter(Line.user.in_([current_user]))
	files_marked = set([line.file for line in lines_marked])

	#figure out total assignments in dataset
	totals = {}
	for assignment in os.listdir(DATA_PATH):
		if not os.path.isdir(os.path.join(DATA_PATH, assignment)):
			continue
		stuff = os.listdir(os.path.join(DATA_PATH, assignment))
		totals[assignment] = len(stuff)

	#figure out actual already labeled by the user
	actual = {key:totals[key] for key in totals}
	for file in files_marked:
		for assignment in actual:
			if assignment.lower() in file:
				actual[assignment] -= 1

	return render_template("menu.html", totals=totals, actual=actual)

@app.route("/label/<filename>")
def show_code(filename):	

	if not session.get("username"):
		flash("You're not logged in!")
		return redirect("/login")

	assignments = os.listdir(DATA_PATH)
	for assignment in assignments:
		if assignment.lower() in filename:
			break

	#read in the appropriate code file
	full_path_fname = os.path.join(DATA_PATH, assignment, filename)
	if not os.path.exists(full_path_fname):
		flash("You can't label <{}> because it doesn't exist.".format(filename))
		return redirect("/menu")

	with open(os.path.join(DATA_PATH, assignment, filename)) as f:
		lines = f.readlines()
		lines = list(filter(lambda x: not x.isspace(), lines))
		lines = [line.replace("\n","<br>").replace("    ","&nbsp;"*4).replace("\t","&nbsp;"*4) for line in lines]
	
	#read user labels from the database
	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(Label).filter(Label.user.in_([session['username']])).order_by(Label.letter)
	results = [q.__dict__ for q in query.all()]

	return render_template("code.html", code=lines, results=results)

@app.route("/submit_code", methods=['POST'])
def handle_submit():

	if 'logged_in' in session and not session['logged_in']:
		return abort("excuse you, you need to be logged in", 404)

	Session = sessionmaker(bind=engine)
	s = Session()

	if "lineForm" in request.form:
		results = {}
		for key,val in request.form.items():
			if key.isdigit():
				print("The line", key, "was marked as extraneous by " + str(session['username'] + "."))
				line = Line(session['username'], "hw3_69.py", key, val)
				s.add(line)
		s.commit()
		return show_code()

	elif "typeForm" in request.form:
		l = Label(session['username'], request.form['letter'], request.form['desc'])
		s.add(l)
		s.commit()
		return show_code()

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)
