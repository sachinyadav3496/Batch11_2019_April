from flask import Flask, render_template
app = Flask(__name__)
import os
BASE_PATH = os.getcwd()
DATA_PATH = os.path.join(BASE_PATH,"static\\data\\")
import json
@app.route("/home/")
@app.route("/")#controller
def index():
    title = "HOME"
    path  = os.getcwd()
    data = [path, "sachin","rajat","kushal","manish","yadvendra","nidhi","gaurav","ravi","akhlish"]

    return render_template("index.html",title=title,data=data)

@app.route("/data/")
def data():
    title = "DATA"
    path = os.path.join(DATA_PATH,"1001.json")
    f = open(path)
    data = json.load(f)
    f.close()

    # data = { 
    #     'Name' : "Python",
    #     "Father" : "Guido Van Rossum",
    #     "Current Version" : 3.7,
    #     "Official Site" : "python.org",
    #     "Package Site" : "pypi.org",
    #     "Use For " : [ "Data Science","Web Designing","Hacking"]
    # }
    return render_template("data.html",title=title,data=data)


@app.route("/user/<string:name>/")
@app.route("/user/")
def user(name=None):
    user = name
    return render_template("user.html",title="user data",user=user)


if __name__ == "__main__" : 
    app.run(debug=True)