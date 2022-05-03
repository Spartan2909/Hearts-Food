from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, IntegerField, validators
import datetime

#App Setup
app = Flask('hearts_food',
    template_folder = 'templates',
    static_folder = 'static'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data.db'
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

    orderDate = db.Column(db.DateTime, nullable=False)

    ticketID = db.Column(db.Integer, db.ForeignKey(Ticket.ticketNum), nullable=False)

    choices = db.relationship('Choice', backref='order', lazy=True)
    payments = db.relationship('Payment', backref='order', lazy=True)
	
class Option(db.Model):
	optionID = db.Column(db.String(25), primary_key=True)
	optionName = db.Column(db.String(35), nullable=False)
	price = db.Column(db.Float, nullable=False)

class Choice(db.Model):
    orderNum = db.Column(db.Integer, db.ForeignKey(Order.orderNum), primary_key=True)
    optionID = db.Column(db.String(25), db.ForeignKey(Option.optionID), primary_key=True)
    
class Payment(db.Model):
    cardNum = db.Column(db.String(16), primary_key=True)
    cvc = db.Column(db.String(4), nullable=False)
    expDate = db.Column(db.DateTime, nullable=False)
    holderName = db.Column(db.String(45), nullable=False)
    totalPrice = db.Column(db.Float, nullable=False)
	
    orderID = db.Column(db.Integer, db.ForeignKey(Order.orderNum), nullable=False)

#Common Functions

def isHotFood(item):
    hot = ['Burger', 'Pie']
    for hotThing in hot:
        if hotThing in item:
            return True
    return False

def isColdFood(item):
    cold = ['Biscuit']
    for coldThing in cold:
        if coldThing in item:
            return True
    return False
	
#Forms

def ticket_valid(form, field):
    selectedTicket = Ticket.query.filter_by(ticketNum=field.data).first()
    if selectedTicket is None:
        raise validators.ValidationError('Ticket does not exist')
    elif selectedTicket.matchDate < datetime.datetime.now().date():
        validators.ValidationError('Ticket is out of date')

class TicketForm(Form):
    ticketNum = StringField('Please enter your ticket number', validators=[validators.DataRequired(), ticket_valid])

class PaymentForm(Form):
    cardNum = IntegerField('Please enter your card number', validators=[validators.DataRequired()])

class OrderSelectForm(Form):
    orderNum = StringField(None, validators=[validators.DataRequired()])
	
#Errors

class error:
    e404 = 'The requested page was not found on the server'
    e405 = 'Invalid request type. Expected {0}, got {1}'
    e500 = 'Internal server error'

#Pages

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        session['ticket']
    except KeyError:
        print('index: redirected to ticket')
        return redirect('/ticket')
    else:
        return render_template('index.html')

@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    form = TicketForm(request.form)
    if request.method == 'POST' and form.validate():
        print('ticket: validated')
        session['ticket'] = form.ticketNum.data
        return redirect('/')

    return render_template('ticket.html', form=form)

@app.route('/food', methods=['GET', 'POST'])
def food():
    options = Option.query.all()
    foodHot = {option.optionID: option.optionName for option in options if isHotFood(option.optionID)}
    foodCold = {option.optionID: option.optionName for option in options if isColdFood(option.optionID)}
    return render_template('food.html', foodHot=foodHot, foodCold=foodCold)

@app.route('/drink')
def drink():
    options = Option.query.all()
    drinkHot = {option.optionID: option.optionName for option in options if 'Hot' in option.optionID}
    drinkCold = {option.optionID: option.optionName for option in options if 'Cold' in option.optionID}
    return render_template('drink.html', drinkHot=drinkHot, drinkCold=drinkCold)

@app.route('/add', methods=['POST'])
def add():
    print(f'add: adding items to basket from origin {request.args.get("origin")}')
    data = request.get_json
    return redirect(f'/{request.args.get("origin")}')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    form = PaymentForm(request.form)
    return render_template('payment.html', form=form)

@app.route('/staff', methods=['GET', 'POST'])
def staff():
    #Use OrderSelectForm to redirect to /staff?ordernum=selectedField
        try:
            orderNum = request.args['ordernum']
            choices = Choice.query.filter_by(orderNum=orderNum).all()
            orderItems = []
            for choice in choices:
                orderItems.append(Option.query.filter_by(optionID=choice.optionID).first())

            return render_template('staff.html', orderView=True, orderNum=orderNum, orderItems=[item.optionName for item in orderItems])

        except KeyError:
            choices = Choice.query.all()
            orders = {}
            for choice in choices:
                if choice.optionID in orders:
                    orders[choice.optionID] += 1
                else:
                    orders[choice.optionID] = 1

            orderNames = orders.copy()
            for order in orderNames:
                orderNames[order] = Option.query.filter_by(optionID=order).first().optionName

            return render_template('staff.html', orderView=False, orderItems={orderNames[orderID]: orderNum for (orderID, orderNum) in orders.items()})

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