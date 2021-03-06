import os


from flask import Flask, request, render_template, redirect, url_for

project_root = os.path.dirname(os.path.realpath('__file__'))
# print(os.path.realpath('__file__'))
template_path = os.path.join(project_root, '../trulinews.com/Templates')
static_path = os.path.join(project_root, '../trulinews.com/static')
app = Flask(__name__,template_folder=template_path,static_folder=static_path)

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

@app.route('/Story1')
def home():
	# send_dict = get_cs(story_num)
	send_dict  = {"main_image":"static/images/blueprint.jpg",
	"title":"Trump Bombs Iran",
	"abstract":"President Trump bombs Iran.","header":"mediabias,source,similarity,sentiment",
	"link":"https://www.google.com",
	"kws":"Trump, Iran"}
	return render_template("../trulinews.com/Templates/news_template.html",send_dict=send_dict)




application = app
if __name__=="__main__":
	app.run()