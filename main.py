from flask import Flask, redirect, render_template, request, jsonify
import requests
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.post("/form")
def file():
    media = request.files["reference"]
    file_available = False
    if media:
        file_available = True
    files = {
        "media": (secure_filename(media.filename), media.stream, media.content_type, media.headers)
    }

    data = request.form.to_dict(flat=True)

    data["file_available"] = file_available

    resp = requests.post(
        "https://ramn8n.onrender.com/webhook/eedbf18e-1904-4105-b9bf-67d51454b0cd",
        files = files,
        data = data,
        timeout = 60
    )

    return jsonify({"status": resp.status_code, "text": resp.text}), resp.status_code

@app.route("/works")
def works():
    return render_template("works.html")

if "__main__" == __name__:
    app.run()