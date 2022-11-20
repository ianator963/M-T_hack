from flask import Flask, render_template
from tkinter import * 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

if __name__ == '__main__': 
   app.run(port=5000, debug=True)
   root = Tk()
