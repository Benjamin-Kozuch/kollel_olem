from flask import Flask, render_template, flash
from flask import redirect, url_for, session, request, logging
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/kollelolam1'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username






@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about(): #  For a donor to make a user account
    return render_template('about.html')

@app.route('/sign_up')
def sign_up(): #  For a donor to make a user account
    return render_template('sign_up.html')

@app.route('/apply')
def apply(): #  For a kollel to apply to recieve donations
    return render_template('apply.html')

@app.route('/log_in')
def log_in(): #  For a kollel to apply to recieve donations
    return render_template('log_in.html')

@app.route('/kollels')
def kollels():
    return render_template('kollels.html')

@app.route('/kollel/<string:id>')
def kollel(id):
    #Each kollel should have a big picture, number of avreichim, Rosh Kollel,
    #Length of existence, what theyre currently learning
    return render_template('kollel.html',id=id)

@app.route('/donate')
def donate():

    #If logged in
    return render_template('donate.html')

    #If not logged in
    return render_template('log_in.html')









if __name__ == '__main__':
    app.run()
