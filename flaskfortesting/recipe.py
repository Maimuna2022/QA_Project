from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'HCCJNC38BDHE77DCS'


class UserInfo(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), length(min=2, max=15)])
    last_name = StringField('Last name', validators=[DataRequired(), length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, max=16)])
    submit = SubmitField('signup')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ""
    signup_form = UserInfo()

    if request.method == 'POST':

        if signup_form.validate_on_submit():

            first_name = signup_form.first_name.data
            last_name = signup_form.last_name.data
            email = signup_form.email.data
            password = signup_form.password.data

            message = f"Welcome {first_name} {last_name} to your account."
        else:
            message = ""
    else:
        message = ""
        signup_form.first_name.data = ""
        signup_form.last_name.data = ""
        signup_form.email.data = ""
        signup_form.password.data = 0

    return render_template("signup.html", form=signup_form, boolean=True)

def read():
    all_users = users.query.all()
    all_users_string = ""
    for user in all_users:
        all_users_string += "<br>"+ user.name
    return all_users_string

def update(user):
    user = Users.query.first()
    user.name = name
    db.session.commit()
    return user.name


class UserLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, max=16)])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    login_form = UserLogin()

    if request.method == 'POST':

        if login_form.validate_on_submit():

            username = login_form.username.data
            password = login_form.password.data

            message = f"Welcome {username} to your account."
        else:
            message = ""
    else:
        message = ""
        login_form.username.data = ""

    return render_template("login.html", form=login_form, boolean=True)


@app.route('/logout')
def logout():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
