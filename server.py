from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'asecretkey'

@app.route('/')
def index():
  if not 'total_gold' in session:
    session['total_gold'] = 0
  # session.pop('total_gold')
  return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
  building_chosen = request.form['building']

  # if farm +10-20 gold
  if building_chosen == 'farm':
    gold_earned = random.randrange(1, 21)

  # if cave +5-10 gold
  elif building_chosen == 'cave':
    gold_earned = random.randrange(5, 11)

  # if house +2-5 gold
  elif building_chosen == 'house':
    gold_earned = random.randrange(2, 6)

  # if casino +/-50 gold
  elif building_chosen == 'casino':
    plus_or_minus = random.randrange(0, 2)
    if plus_or_minus == 0:
      gold_earned = -50
    else:
      gold_earned = 50

  print gold_earned
  session['total_gold'] += gold_earned

  return redirect('/')

app.run(debug=True)

