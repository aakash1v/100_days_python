from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(blog_url).json()
post_objects = []

for post in posts:
    print(post)
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/blogs/')
def get_all_posts():
    return render_template("index.html", posts =posts)


@app.route('/post/<int:index>')
def one_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template('post.html', post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
