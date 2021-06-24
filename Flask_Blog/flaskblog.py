from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Tony Lacson',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 23, 2021'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 24, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


# Allows this file to be run with just 'py flaskblog.py' without setting environment variables and using 'flask run':
# FLASK_APP
# FLASK_DEBUG
if __name__ == '__main__':
    app.run(debug=True)