from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/submit-form.php")
def world1():
    return render_template('index1.html')




