from flask import Flask, session, redirect, url_for, escape, request, render_template
import re
from import1 import wordstring, process

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
#
#
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def index():
    #if 'blacks' in session:
    if request.method == 'POST':
        session['blacks'] = request.form['blacks'].lower()
        if len(session['blacks'])==0:
            session['blacks'] = ' '
        session['greens'] = (request.form['greens'].lower() + '-----')[:5]
        session['yellows'] = request.form['yellows'].lower()
        hints = process(session['blacks'], session['yellows'], session['greens'])
        return render_template('input_colors.html', hints=hints, blacks=session['blacks'], yellows=session['yellows'], greens=session['greens'])
    else:
        return render_template('input_colors.html', greens='-----')

    #return 'You are not logged in : ' + '<a href="' + url_for('login') + '">input blacks</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['blacks'] = request.form['blacks']
        session['greens'] = request.form['greens']
        return redirect(url_for('index'))
    return render_template('input_colors.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('blacks', None)
    return redirect(url_for('index'))

