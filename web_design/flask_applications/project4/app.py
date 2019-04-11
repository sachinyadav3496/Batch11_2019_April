from flask import Flask, render_template,request
import os 
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",title="home")


@app.route("/login/",methods=["POST","GET"])
def login():
    if request.method == "POST"  : 
        email = request.form['email']
        password = request.form['password']
        if len(email) > 5 and len(password) > 8 : 

            data = {
                'email' : email ,
                'Password' :  password }
            return render_template("profile.html",title="profile",info=data,flag=True)
        else : 
            error = "Length of UserName and Password Should Be greater."
    else : 
        error = "Please Login First to Continue"
    return render_template("index.html",title='home',error=error)
@app.route("/signup/")
def signup():
    return render_template("signup.html")


@app.route("/mksignup/",methods=["GET","POST"])
def mksignup():
    if request.method == "POST" : 
        data = { 
            'User Name' : request.form['username'],
            'First Name' : request.form['fname'],
            'Last Name' : request.form['lname'],
            'Email' : request.form['email'],
            'Phone Number' : request.form['ph_no'],
            'Password' : request.form['password'],
            'img_path' : ''
        }

        return render_template("mksignup.html",data=data,title="Profile")
    else : 
        error = "Method Not Allowed"
        return render_template("signup.html",error=error)
if __name__ == "__main__" : 
    app.run(debug=True)