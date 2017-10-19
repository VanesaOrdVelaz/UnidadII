from square import square_perimeter
from flask import Flask, render_template, redirect, request

app = Flask (__name__)

@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry/')
def go_entry() -> 'html':
    return render_template('entry.html', the_title='Welcome',)

@app.route("/calculate/", methods=['POST'])
def calculate() -> 'html':
    a = float(request.form['a'])
    result = square_perimeter(a)
    title = "Square Perimeter result"
    return render_template('results.html', the_a=a, the_result= result, the_title=title)

app.run(debug=True)