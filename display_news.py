import os
import pandas as pd
import json
from flask import Flask, request, render_template, redirect, url_for

project_root = os.path.dirname(os.path.realpath('__file__'))
# print(os.path.realpath('__file__'))
# template_path = os.path.join(project_root, 'templates')
# static_path = os.path.join(project_root, '../trulinews.com/static')
app = Flask(__name__)

"""
main_image
kws
title
abstract
link
sentiment
media bias score
source
similarity
"""

stories = []
media_bias_paths = []
for story in range(5):
	df = pd.read_csv("stories/story_"+str(story)+".csv")
	stories.append(json.loads(df.to_json()))
	media_bias_paths.append(json.loads(df["name"].to_json()))

@app.route('/Story1')
def home():
	# send_dict = get_cs(story_num)
	# send_dict  = {"main_image":"static/images/blueprint.jpg",
	# "title":"Trump Bombs Iran",
	# "abstract":"President Trump bombs Iran.",
	# "mediabias":"static/images/im1.png",
	# "similarity":"static/images/im2.jpg",
	# "sentiment":"static/images/im3.jpg",
	# "source":"CNN",
	# "link":"https://www.google.com",
	# "kws":"Trump, Iran"}
	return render_template("news_template.html",send_dict=stories[0],media_bias_paths=media_bias_paths[0])


@app.route('/Story2')
def home():
	# send_dict = get_cs(story_num)
	# send_dict  = {"main_image":"static/images/blueprint.jpg",
	# "title":"Trump Bombs Iran",
	# "abstract":"President Trump bombs Iran.",
	# "mediabias":"static/images/im1.png",
	# "similarity":"static/images/im2.jpg",
	# "sentiment":"static/images/im3.jpg",
	# "source":"CNN",
	# "link":"https://www.google.com",
	# "kws":"Trump, Iran"}
	return render_template("news_template.html",send_dict=stories[1],,media_bias_paths=media_bias_paths[1])


@app.route('/Story3')
def home():
	# send_dict = get_cs(story_num)
	# send_dict  = {"main_image":"static/images/blueprint.jpg",
	# "title":"Trump Bombs Iran",
	# "abstract":"President Trump bombs Iran.",
	# "mediabias":"static/images/im1.png",
	# "similarity":"static/images/im2.jpg",
	# "sentiment":"static/images/im3.jpg",
	# "source":"CNN",
	# "link":"https://www.google.com",
	# "kws":"Trump, Iran"}
	return render_template("news_template.html",send_dict=stories[2],,media_bias_paths=media_bias_paths[2])


@app.route('/Story4')
def home():
	# send_dict = get_cs(story_num)
	# send_dict  = {"main_image":"static/images/blueprint.jpg",
	# "title":"Trump Bombs Iran",
	# "abstract":"President Trump bombs Iran.",
	# "mediabias":"static/images/im1.png",
	# "similarity":"static/images/im2.jpg",
	# "sentiment":"static/images/im3.jpg",
	# "source":"CNN",
	# "link":"https://www.google.com",
	# "kws":"Trump, Iran"}
	return render_template("news_template.html",send_dict=stories[3],media_bias_paths=media_bias_paths[3])

@app.route('/Story5')
def home():
	# send_dict = get_cs(story_num)
	# send_dict  = {"main_image":"static/images/blueprint.jpg",
	# "title":"Trump Bombs Iran",
	# "abstract":"President Trump bombs Iran.",
	# "mediabias":"static/images/im1.png",
	# "similarity":"static/images/im2.jpg",
	# "sentiment":"static/images/im3.jpg",
	# "source":"CNN",
	# "link":"https://www.google.com",
	# "kws":"Trump, Iran"}
	return render_template("news_template.html",send_dict=stories[4],media_bias_paths=media_bias_paths[4])



application = app
if __name__=="__main__":
	app.run()