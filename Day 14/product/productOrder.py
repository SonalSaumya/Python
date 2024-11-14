from flask import Flask, render_template, request, redirect, url_for, session

appLogin = Flask(__name__)
appLogin.secret_key = 'secret'

print(appLogin)


@appLogin.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        quantity= request.form.get('quantity')
        session['product_name'] =product_name
        session['quantity'] = quantity
        return redirect(url_for('shipping'))
    return render_template('home.html')


@appLogin('/shipping', methods=['GET','POST'])
def shipping():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        contact = request.form.get('contact')

        session['name'] = name
        session['address'] = address
        session['contact'] = contact
        return redirect(url_for('summary'))
    return render_template('shipping.html')


def summary():
    product_name = session.get('product_name')
    quantity = session.get('quantity')
    name = session.get('name')
    address = session.get('address')
    contact = contact.get('contact')
    return render_template('shipping.html', product_name=product_name, quantity=quantity, name=name, address=address,contact=contact)


@appLogin('/confirm')
def confirm():
    return render_template('confirm.html')


if __name__ == '__main__':
    appLogin.run(debug=True)
