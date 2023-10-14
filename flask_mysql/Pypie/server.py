from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy(app)

# Models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    pies = db.relationship('Pie', backref='user')

    def __repr__(self):
        return f'<User {self.username}>'

class Pie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    crust = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Pie {self.name}>'

# Forms

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[validators.Length(min=3)])
    last_name = StringField('Last Name', validators=[validators.Length(min=3)])
    email = StringField('Email', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[validators.EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.Email()])
    password = PasswordField('Password')
    submit = SubmitField('Login')

class PieForm(FlaskForm):
    name = StringField('Pie Name', validators=[validators.Length(min=3)])
    crust = StringField('Crust', validators=[validators.Length(min=3)])
    submit = SubmitField('Add Pie')

# Controllers

@app.route('/', methods=['GET', 'POST'])
def index():
    register_form = RegisterForm()
    login_form = LoginForm()

    if register_form.validate_on_submit():
        user = User(username=register_form.first_name.data + register_form.last_name.data, email=register_form.email.data, password=register_form.password.data)
        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        return redirect(url_for('dashboard'))

    elif login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and user.check_password(login_form.password.data):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

    return render_template('index.html', register_form=register_form, login_form=login_form)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    user = User.query.get(session['user_id'])
    pies = Pie.query.filter_by(user_id=user.id).all()

    return render_template('dashboard.html', user=user, pies=pies)

@app.route('/edit/<int:pie_id>', methods=['GET', 'POST'])
def edit(pie_id):
    if 'user_id' not in session:
        return redirect(url_for('index'))

    pie = Pie.query.get(pie_id)
    if pie.user_id != session['user_id']:
        return redirect(url_for('dashboard'))

    form = PieForm(name=pie.name, crust=pie.crust)