from flask import Flask, render_template, request, redirect, url_for

ageChecker = Flask(__name__)
print(ageChecker)

@ageChecker.route('/')
def age():
    return render_template("age.html")

@ageChecker.route('/check_age',methods=['POST'])
def check_age():
  if request.method == 'POST':
    name = request.form['name']
    age = int(request.form['age'])

    return redirect(url_for('result', name=name, age=age))

         return "you are a minor."

@ageChecker.route('/dashboard')
def show_dashboard():
    return render_template("dashboard.html")


if __name__=='__main__':
    ageChecker.run(debug=True)
