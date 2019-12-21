from flask import Flask,render_template,request
from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
