from flask import Flask, render_template, request, redirect, url_for

spage = Flask(__name__)
print(spage)

@spage.route('/')
def home():
    return render_template("home.html")

@spage.route('/home',methods=['POST'])
def survey():
    return redirect(url_for('show_survey'))


@spage.route('/survey')
def show_survey():
    return render_template("survey.html")


@spage.route('/result', methods=['POST'])
def show_result():
    return render_template("result.html")



if __name__=='__main__':
    spage.run(debug=True)