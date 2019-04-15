from flask import Flask,render_template,request,url_for,flash,redirect

app = Flask(__name__)

app.secret_key = b'b_5#@13jouaf/r9usjf'

@app.route("/")
def index():
    return render_template('index.html',title='HOME')


@app.route("/signup/")
def signup():
    return render_template("signup.html",title="Signup")
if __name__ == "__main__" : 
    app.run(debug=True)
