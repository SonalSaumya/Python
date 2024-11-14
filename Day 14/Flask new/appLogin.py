from flask import Flask, render_template, request, redirect, url_for

appLogin = Flask(__name__)
print(appLogin)

@appLogin.route('/')
def login():
    return render_template("login.html")

@appLogin.route('/login',methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    if username=='admin' and password=='password':
        #return f"welcome {username}"
        return redirect(url_for('show_dashboard'))
    else:
        return "Invalid"

@appLogin.route('/dashboard')
def show_dashboard():
    return render_template("dashboard.html")


if __name__=='__main__':
    appLogin.run(debug=True)
