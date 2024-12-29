from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, Text, select, create_engine
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField  
from datetime import date, datetime
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'posts.db')}"
os.makedirs(app.instance_path, exist_ok=True)
Bootstrap5(app)
ckeditor = CKEditor(app)



# CREATE DATABASE
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# Create engine and session
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

with app.app_context():
    db.create_all()

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # use CKEditor
    # body = CKEditorField("Blog Content", validators=[DataRequired()])
    body = TextAreaField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = session.scalars(select(BlogPost)).all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = session.scalars(select(BlogPost).where(BlogPost.id == post_id)).first()
    return render_template("post.html", post=requested_post)            


# TODO: add_new_post() to create a new blog post
@app.route('/add-post', methods=['POST', 'GET'])
def add_new_post():
    form = CreatePostForm()
    today = datetime.now()
    # if form.validate_on_submit(): 
    if request.method == 'POST':
        new_post = BlogPost(
            title=form.title.data,
            date=today.strftime("%a %d, %Y"),
            author=form.author.data, 
            subtitle=form.subtitle.data,
            img_url=form.img_url.data,
            body=form.body.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))   

    return render_template("create_post.html", form=form)

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("create_post.html", form=edit_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
