from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'asecretkey'

@app.route('/')
def index():
  return 'hello werld'

app.run(debug=True)

