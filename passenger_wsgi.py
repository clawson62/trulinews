import os

from flask import Flask, request, render_template, redirect, url_for

project_root = os.path.dirname(os.path.realpath('__file__'))
# template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder="Templates", static_folder=static_path)

@app.route('/')
def home():
    return render_template("index.html")


application = app