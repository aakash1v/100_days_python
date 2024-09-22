from flask import Flask, render_template
import requests
from blog import Blog

app = Flask(__name__)
blog_url = 'https://api.npoint.io/23904b05c7e801d53831'
response = requests.get(blog_url)
all_post = response.json()
my_blogs = []

for post in all_post:
    new_post = Blog(post['id'], post['title'], post['subtitle'], post['body']) 
    my_blogs.append(new_post)

# print(my_blogs[0].title)

@app.get('/')
def home():
    return render_template('index.html', posts=my_blogs) 

@app.get('/about')
def about():
    return render_template('about.html')
 
@app.get('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog in my_blogs:
        if blog.id == index:
            requested_post = blog

    # Setting image url for different blogs...

    if index ==1:
        image_url = '../static/assets/img/cactus.jpg'
    elif index ==2:
        image_url  =  '../static/assets/img/bored.jpg'
    else:
        image_url = '../static/assets/img/fasting.jpg'
    return render_template('post.html', post=requested_post, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)