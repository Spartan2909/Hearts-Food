from flask import Flask, render_template, redirect, url_for, request, session
from python import error, options, forms

#App Setup

app = Flask('app',
    template_folder = 'templates',
    static_folder = 'static'
)

app.config['SECRET_KEY'] = r'-O/*/|#~mD]=_eeeRl(e#=hbh4a8Y$'

#Pages

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.TicketForm(request.form)
    if request.method == 'POST' and form.validate():
        session['code'] = form.code.data
        return redirect(url_for('select'))

    return render_template('index.html', form=form)

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
    app.run(host='0.0.0.0', port=8080)
