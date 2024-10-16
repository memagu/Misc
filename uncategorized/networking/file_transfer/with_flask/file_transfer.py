import os
import time

from flask import Flask, request, render_template, redirect, send_from_directory

# DOWNLOAD_DIR = r"C:/Users/melke/AppData/Local/FactoryGame/Saved/SaveGames/f494e05699ca41b090c172f7cc70163f"
DOWNLOAD_DIR = r"C:\Users\melke\Desktop\Share"

app = Flask(__name__)

# app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template("index.html", files=os.listdir(DOWNLOAD_DIR))


# TODO redirect to home
@app.route('/<file>')
def download(file):
    print(file)
    return send_from_directory(DOWNLOAD_DIR, file, as_attachment=True)


@app.route('/', methods=['POST'])
def upload_file():
    start = time.perf_counter()
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save("in/" + uploaded_file.filename)
    end = time.perf_counter()
    return f"{uploaded_file.filename} uploaded in {end - start:.6f}s"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=443, ssl_context=("./ssl/certificate.pem", "./ssl/private.pem"))
