from flask import Flask, render_template,request
import os,json
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
USER_DATA = os.path.join(BASE_DIR,"static\\data")
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
            tmp_path = "users\\"+email.strip()+".json"
            path = os.path.join(USER_DATA,tmp_path)
            if os.path.exists(path) : 
                return "Sucess"
            else :
                error = "No such User Exists, Please Signup First" 
                return render_template("index.html",title="home",error=error)
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
        email = request.form['email']
        new_path = "users\\"+email.strip()+ ".json"
        path = os.path.join(USER_DATA,new_path)
        if os.path.exists(path):
            error = "User Already Exists Please Signin to Enjoy Your Services"
            return render_template("index.html",error=error,title='home')
        else : 
            file = request.files['pic']
            #if file.filename.split('.')[-1] in [ 'jpg','jpeg','png',]
            tmp_path = "users_profile\\"+email.strip()+".jpg"
            filename = os.path.join(USER_DATA,tmp_path)
            file.save(filename)
            data = { 
                'User Name' : request.form['username'],
                'First Name' : request.form['fname'],
                'Last Name' : request.form['lname'],
                'Email' : request.form['email'],
                'Phone Number' : request.form['ph_no'],
                'Password' : request.form['password'],
                'img_path' : filename,
            }
            f = open(path,'w')
            json.dump(data,f)
            f.close()
            error = "Account Successfully Created Please Login Now"
            return render_template("index.html",title="Profile",error=error)
    else : 
        error = "Method Not Allowed"
        return render_template("signup.html",error=error)
if __name__ == "__main__" : 
    app.run(debug=True)