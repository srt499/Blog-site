from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/48cb0be6cc67f7dc34fc').json()
all_posts = []
for post in posts:
    all_posts.append(post)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def get_blog(num):
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == num:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
