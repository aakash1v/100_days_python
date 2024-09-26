from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Log in ')


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST' ])
def login():
    form = MyForm()
    form.validate_on_submit()
    if request.method == "POST":
        if form.email.data=='aakashkumarpy@gmail.com' and form.password.data == '123' :
            print(form.email.data)
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
