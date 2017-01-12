from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'asecretkey'

@app.route('/')
def index():
  if not 'gold_count' in session:
    session['gold_count'] = 0
  return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
  building_chosen = request.form['building']

  # if farm +10-20 gold
  if building_chosen == 'farm':

  # if cave +5-10 gold
  elif building_chosen == 'cave':
  # if house +2-5 gold
  elif building_chosen == 'house':
  # if casino +/-50 gold
  elif building_chosen == 'casino':

  return redirect('/')

app.run(debug=True)

