from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'asecretkey'

@app.route('/')
def index():
  return render_template('index.html')

app.run(debug=True)

