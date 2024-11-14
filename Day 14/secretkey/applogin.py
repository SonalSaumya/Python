from flask import Flask, render_template, request, redirect, url_for, session

appLogin = Flask(__name__)
appLogin.secret_key = 'secret'

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
        session['name'] = username
        return redirect(url_for('show_dashboard'))
    else:
        return "Invalid"

@appLogin.route('/dashboard')
def show_dashboard():
    name = session.get('name')
    return render_template("dashboard.html")


if __name__=='__main__':
    appLogin.run(debug=True)
