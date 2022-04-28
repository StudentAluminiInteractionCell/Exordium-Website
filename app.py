from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/saic'


class Regis_form(db.Model):
    rno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    p_rno = db.Column(db.Integer, nullable=False)
    p_name = db.Column(db.String(50), nullable=False)
    p_email = db.Column(db.String(100), nullable=False)
    talent = db.Column(db.String(255), nullable=False)
    screen_name = db.Column(db.String(100), nullable=False)
    movie_line = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(20), nullable=False)


@app.route("/", methods=['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        rno = request.form.get('rno')
        name = request.form.get('name')
        email = request.form.get('email')
        p_rno = request.form.get('p_rno')
        p_name = request.form.get('p_name')
        p_email = request.form.get('p_email')
        talent = request.form.get('Q1')
        screen_name = request.form.get('Q2')
        movie_line = request.form.get('Q3')

        entry = Regis_form(rno=rno, name=name, email=email, p_rno=p_rno, p_name=p_name, p_email=p_email,
                           talent=talent, screen_name=screen_name, movie_line=movie_line, date=datetime.now())

        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')


app.run(debug=True)
