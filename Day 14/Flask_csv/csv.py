from flask import Flask, render_template, request, redirect, url_for

appLogin = Flask(__name__)
print(appLogin)

@appLogin.route('/')
def path():
    return render_template("path.html")



if __name__=='__main__':
    appLogin.run(debug=True)
