from flask import session,Flask,render_template,request,url_for,flash,redirect
import MySQLdb as sql 
app = Flask(__name__)

app.secret_key = b'b_5#@13jouaf/r9usjf'

def connect(user,password,dbname):
    con = sql.connect(host='localhost',port=3306,
    user=user,password=password,database=dbname)
    cur = con.cursor()
    return con,cur 


@app.route("/")
def index():
    if 'email' in session and session['email'] :
        email  = session['email']
        con,cur = connect(user='project1',password='redhat',dbname='project1')
        cur.execute(f"select * from user where email='{email}'") 
        data  = cur.fetchone() 
        img = data[4]
        data = { 
                    'Email' : data[0],
                    'First Name' : data[1],
                    'Last Name' : data[2],
                }
                
        return render_template('profile.html',flag=True,data=data,img=img)
    else : 
        return render_template('index.html',title='HOME')


@app.route("/signup/")
def signup():
    return render_template("signup.html",title="Signup")

@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "POST" : 
        email = request.form['email']
        password = request.form['password']
        con,cur = connect('project1','redhat','project1')
        # cur.execute(f"select * from user where email='{email}' and password='{password}'")
        cur.execute(f"select email from user")
        data = cur.fetchall()
        data = [ email[0] for email in data ]
        print(data)
        if email in data :
            cur.execute(f"select * from user where email='{email}'") 
            data  = cur.fetchone()
            if data[3] == password :
                session['email'] = email 
                img = data[4]
                data = { 
                    'Email' : data[0],
                    'First Name' : data[1],
                    'Last Name' : data[2],
                }
                
                return render_template('profile.html',data=data,img=img,flag=True)
            else : 
                flash("Invalid Password") 
        else : 
             flash("No such Account Exists")
    else : 
        flash("Invalid Form Method")
    
    return redirect(url_for("index"))


@app.route('/logout/')
def logout():
    session.pop('email',None)
    flash("Logout successfully")
    return redirect(url_for('index'))
if __name__ == "__main__" : 
    app.run(debug=True)
