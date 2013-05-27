# Run this app to test strip connect
# Start it with your keys in the command line - e.g:
# PUBLISHABLE_KEY=pk_test_YOURKEY SECRET_KEY=sk_test_YOURKEY python app.py

import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    amount = 350

    customer = stripe.Customer.create(
        email='tom@susweb.net',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='eur',
        description='a charge in dollars'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)