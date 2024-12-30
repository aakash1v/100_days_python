from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Select
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = './static/files'


# Configure Flask-Login's Login Manager

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()




@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register',methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        already_email = db.session.execute(Select(User).where(User.email == email)).scalar()

        # already existing emaill....
        print(already_email)
        if already_email:
            flash("You've have already signed up with this email,login instead.")
            return redirect(url_for("login"))

        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='scrypt', salt_length=16)
        new_user = User(
            name = request.form.get('name'),
            email = request.form.get('email'),
            password = hashed_password
            )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login' ,methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.execute(Select(User).where(User.email==email)).scalar()

        if not user:
            flash("This email doesn't exist , Please register..")
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again...!")
        else:
            login_user(user)
            return redirect(url_for('secrets'))
        
    return render_template("login.html", logged_in=current_user.is_authenticated) 


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf', as_attachment=True )


if __name__ == "__main__":
    app.run(debug=True)
