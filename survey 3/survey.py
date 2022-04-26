from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)

app.secret_key = "shush"

@app.route('/')
def index():
  return render_template("survey_index.html")

@app.route('/results', methods=['POST'])
def create_user():


    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect ('/show_results')

@app.route('/show_results')
def show_results():
    return render_template('survey_results.html')


app.run(debug=True, port=5001)