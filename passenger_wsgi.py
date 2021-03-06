import os
import sys
sys.path.insert(0,'/home/furnixsp/home/trulinews/Templates/')

from flask import Flask, request, render_template, redirect, url_for

project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'Templates')
static_path = os.path.join(project_root, 'Templates')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)

@app.route('/')
def home():
    return render_template("Home.html", **locals())


application = app