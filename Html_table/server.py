from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def list():
    studentsInfo = [
        {'first': 'Logan', 'last': 'Guerra'},
        {'first' : 'Eric', 'last' : 'Cartman'},
        {'first' : 'Stan', 'last' : 'Marsh'}
    ]
    return render_template('index.html', students=studentsInfo)

if __name__=="__main__":
    app.run(debug=True)



