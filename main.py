from flask import Flask, render_template, redirect, url_for, request, session
from wtforms import Form, IntegerField, SelectMultipleField, SubmitField, validators
from python import error, options

#Forms

class TicketForm(Form):
    code = IntegerField('Please enter your ticket number', validators=[validators.DataRequired()])

class FoodForm(Form):
    foodChoices = SelectMultipleField('Choose your food', choices=options.options)

class PaymentForm(Form):
    cardNum = IntegerField('Please enter your card number', validators=[validators.DataRequired()])

#General Functions



#App Setup

app = Flask('app',
    template_folder = 'templates',
    static_folder = 'static'
)

app.config['SECRET_KEY'] = r'-O/*/|#~mD]=_eeeRl(e#=hbh4a8Y$'

#Pages

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TicketForm(request.form)
    if request.method == 'POST' and form.validate():
        session['code'] = form.code.data
        return redirect(url_for('select'))

    return render_template('index.html', form=form)

@app.route('/select', methods=['GET', 'POST'])
def select():
    form = FoodForm(request.form)
    if request.method == 'POST' and form.validate():
        session['choices'] = form.foodChoices.data
        return redirect(url_for('payment'))
    return render_template('select.html', form=form)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    form = PaymentForm(request.form)
    return render_template('payment.html', form=form)

#Errors

@app.errorhandler(404)
def error404(e):
    return render_template('error.html', errorCode=404, message=error.e404)

@app.errorhandler(500)
def error500(e):
    return render_template('error.html', errorCode=500, message=error.e500)

#Run

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)