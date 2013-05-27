stripe-experiments
==================

Experiments with Stripe Checkout and Connect using Flask

## Checkout example

run: `PUBLISHABLE_KEY=pk_test_YOURKEY SECRET_KEY=sk_test_YOURKEY` python app.py

## Connect example

run: `python connect.py`

To make the Connect example work you'll need to add a file call 'keys.cfg' at the root of the repo in this format:

    API_KEY = 'YOUR_SECRET_API_KEY'
    CLIENT_ID = 'YOUR_CLIENT_ID'
