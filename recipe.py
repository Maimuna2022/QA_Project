from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'HCCJNC38BDHE77DCS'


class UserInfo(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, max=16)])
    Login = SubmitField('Login')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("signup.html", boolean=True)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    data = request.form
    print(data)
    return render_template("signup.html", boolean=True)

@app.route('/logout')
def logout():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
