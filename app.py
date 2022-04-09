from flask import Flask, render_template, request
from listAssignments import convert

app = Flask(__name__)

@app.route('/')
def template():
    return render_template('template.html')

@app.route('/', methods=['POST'])
def output():
    input = request.form['input']
    addons = request.form['addons']
    input = input.split('\n')
    processed_text = convert(input, addons)
    processed_text = processed_text.split('\n')
    return render_template('template.html', text=processed_text)