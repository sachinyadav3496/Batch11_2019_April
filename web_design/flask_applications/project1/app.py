from flask import Flask 

app = Flask(__name__)


@app.route("/") # home page
def index():
    return "<h1 style='color:red'>Welcome to First Web Page Powered by Flask</h1>" #reponse




#app.run()
app.run(host="192.168.1.113",port=5000,debug=True)