from wtforms import Form, StringField, SelectMultipleField, SubmitField, validators

class TicketForm(Form):
    code = StringField('Please enter your ticket number', validators=[validators.DataRequired()])

class FoodForm(Form):
    foodChoices = SelectMultipleField('Choose your food', choices=options.options)

class PaymentForm(Form):
    cardNum = IntegerField('Please enter your card number', validators=[validators.DataRequired()])
