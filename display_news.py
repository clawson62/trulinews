import os


from flask import Flask, request, render_template, redirect, url_for

project_root = os.path.dirname(os.path.realpath('__file__'))
# print(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'Templates')
# static_path = os.path.join(project_root, 'static')
app = Flask(__name__,template_folder=template_path)

@app.route('/')
def home():
    return render_template("news_template.html")

# application = app
if __name__=="__main__":
	app.run()