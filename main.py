from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/works")
def works():
    return render_template("works.html")

if "__main__" == __name__:
    app.run()