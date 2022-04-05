# A simple batch script to add new entities to the database
# Must be placed in the same folder as app.py
# Will not be pushed or pulled by git

from app import db, Ticket, Order, Option, Choice, Payment
from datetime import datetime

itemsToAdd = [
Option(optionID='foodPieScotch', optionName='Scotch Pie', price=2.5),
Option(optionID='foodPieSteak', optionName='Steak Pie', price=2.75),
Option(optionID='foodBurgerPlain', optionName='Plain Hamburger', price=2.25),
Option(optionID='foodBurgerCheese', optionName='Cheeseburger', price=2.5),
Option(optionID='drinkHotBovril', optionName='Bovril', price=1.5),
Option(optionID='drinkHotTea', optionName='Tea', price=1.5),
Option(optionID='drinkHotCoffee', optionName='Coffee', price=1.75),
Option(optionID='drinkColdWater', optionName='Water', price=0.0),
Ticket(ticketNum=0, matchDate=datetime(2023, 5, 27), seatNum='A47')
]

for item in itemsToAdd:
    db.session.add(item)
db.session.commit()
