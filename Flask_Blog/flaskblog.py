from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# Allows this file to be run with just 'py flaskblog.py' without setting environment variables and using 'flask run':
# FLASK_APP
# FLASK_DEBUG
if __name__ == '__main__':
    app.run(debug=True)