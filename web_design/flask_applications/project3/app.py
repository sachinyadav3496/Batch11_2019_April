from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",title="home")
@app.route("/login/",methods=["POST","GET"])
def login():
    if request.method == "POST"  : 
        
        username = request.form['username']
        password = request.form['password']
        page = f"""
        <h1> Username = {username} </h1>
        <h2 > Password = {password} </h2>
        <h3>Sucess</h3>
         <a href='/'>HOME</a>"""
        return page 
    else : 
        return render_template("index.html",title='home',error="Please Login First to Continue")
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
        }
        return render_template("mksignup.html",data=data)
    else : 
        error = "Method Not Allowed"
        return render_template("signup.html",error=error)
if __name__ == "__main__" : 
    app.run(debug=True)