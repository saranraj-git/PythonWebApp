from flask import Flask, redirect, url_for  # from flask class, importing Flask() method

app = Flask(__name__)

@app.route("/")    # setting the path for the URL
def home():
    return "Hello! this is the main page <h1> Hello <h1>"

@app.route("/<name>")  # passes the variable "name" from http url to python app as a parameter
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))    # If user enters /admin in url then it will redirect to home()

if __name__ == "__main__":
    app.run()