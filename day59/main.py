from flask import Flask, render_template, request
import requests
import smtplib
from blog import Blog
from dotenv import load_dotenv
import os

load_dotenv()

my_email = 'aakashkumarpy@gmail.com'
password = os.getenv('PASSWORD') 



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
 
@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data['name'])
        print(data['phone'])
        print(data['email'])
        print(data['message'])
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', msg_true=False)
    return render_template('contact.html', msg_true=True)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, my_email, email_message)



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