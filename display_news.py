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
kwds = []
show_images = []
for story in range(5):
	df = pd.read_csv("stories/story_"+str(story)+".csv")
	stories.append(json.loads(df.to_json()))
	kwds.append(str(json.loads(df["kw"].to_json())["0"]).strip("[]").replace(",",", ").replace("'",""))
	media_bias_paths.append(["static/sources/"+i+".png" if str(i) != "None" else "static/images/no_data.png" for i in json.loads(df["name"].to_json()).values()])
	show_images.append([i if "." in str(i) else "static/images/base_image.jpg" for i in json.loads(df["urlToImage"].to_json()).values()])


@app.route('/home')
def home():

	return render_template("index.html")
@app.route('/Story1')
def Story1():
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
	return render_template("news_template.html",send_dict=stories[0],media_bias_path=media_bias_paths[0],kwds=kwds[0],show_images=show_images[0])


@app.route('/Story2')
def Story2():
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
	return render_template("news_template.html",send_dict=stories[1],media_bias_path=media_bias_paths[1],kwds=kwds[1],show_images=show_images[1])


@app.route('/Story3')
def Story3():
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
	return render_template("news_template.html",send_dict=stories[2],media_bias_path=media_bias_paths[2],kwds=kwds[2],show_images=show_images[2])


@app.route('/Story4')
def Story4():
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
	return render_template("news_template.html",send_dict=stories[3],media_bias_path=media_bias_paths[3],kwds=kwds[3],show_images=show_images[3])

@app.route('/Story5')
def Story5():
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
	return render_template("news_template.html",send_dict=stories[4],media_bias_path=media_bias_paths[4],kwds=kwds[4],show_images=show_images[4])



application = app
if __name__=="__main__":
	app.run()