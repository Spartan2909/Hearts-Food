from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, SelectMultipleField, IntegerField, validators

#App Setup
options = []

app = Flask('hearts_food',
    template_folder = 'templates',
    static_folder = 'static'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = r'-O/*/|#~mD]=_eeeRl(e#=hbh4a8Y$'

db = SQLAlchemy(app)

#Database Tables

class Ticket(db.Model):
    ticketNum = db.Column(db.Integer, primary_key=True)
    matchDate = db.Column(db.Date, nullable=False)
    seatNum = db.Column(db.String(6), nullable=False)

    orders = db.relationship('Order', backref='ticket', lazy=True)
	
class Order(db.Model):
    orderNum = db.Column(db.Integer, primary_key=True)

    ticketID = db.Column(db.Integer, db.ForeignKey(Ticket.ticketNum), nullable=False)

    choices = db.relationship('Choice', backref='order', lazy=True)
    payments = db.relationship('Payment', backref='order', lazy=True)
	
class Option(db.Model):
	optionID = db.Column(db.String(25), primary_key=True)
	optionName = db.Column(db.String(35), nullable=False)

class Choice(db.Model):
    orderNum = db.Column(db.Integer, db.ForeignKey(Order.orderNum), primary_key=True)
    optionID = db.Column(db.String(25), db.ForeignKey(Option.optionID), primary_key=True)
    
class Payment(db.Model):
    cardNum = db.Column(db.String(16), primary_key=True)
    cvc = db.Column(db.String(4), nullable=False)
    expDate = db.Column(db.DateTime, nullable=False)
    holderName = db.Column(db.String(45), nullable=False)
    cost = db.Column(db.Float, nullable=False)
	
    orderID = db.Column(db.Integer, db.ForeignKey(Order.orderNum), nullable=False)
	
#Forms

class TicketForm(Form):
    code = StringField('Please enter your ticket number', validators=[validators.DataRequired()])

class FoodForm(Form):
    options = Option.query.all()
    foodChoices = SelectMultipleField('Choose your food', choices=[(option.optionID, option.optionName) for option in options])

class PaymentForm(Form):
    cardNum = IntegerField('Please enter your card number', validators=[validators.DataRequired()])
	
#Errors

class error:
	e404 = 'The requested page was not found on the server'
	e500 = 'Internal server error'

#Pages

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    form = forms.TicketForm(request.form)
    if request.method == 'POST' and form.validate():
        session['code'] = form.code.data
        return redirect(url_for('select'))

    return render_template('ticket.html', form=form)

@app.route('/select', methods=['GET', 'POST'])
def select():
    form = forms.FoodForm(request.form)
    if request.method == 'POST' and form.validate():
        session['choices'] = form.foodChoices.data
        return redirect(url_for('payment'))
    return render_template('select.html', form=form)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    form = forms.PaymentForm(request.form)
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
    app.run(host='0.0.0.0', port=5000)