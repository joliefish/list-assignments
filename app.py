from flask import Flask, render_template, request
from listAssignments import convert

app = Flask(__name__)

@app.route('/')
def template():
    return render_template('template.html')

@app.route('/', methods=['POST'])
def output():
    input = request.form['input']
    processed_text = convert(input)
    return processed_text