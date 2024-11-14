from flask import Flask, render_template, request, redirect, url_for

appLogin = Flask(__name__)
print(appLogin)

@appLogin.route('/')
def login():
    return render_template("login.html")

@appLogin.route('/login',methods=['POST'])
def handle_login():
    return redirect(url_for('show_age'))


@appLogin.route('/age')
def show_age():
    return render_template("age.html")



if __name__=='__main__':
    appLogin.run(debug=True)
