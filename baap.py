from operator import index
from traceback import print_tb
from unittest import result
from winreg import REG_DWORD
from flask import Flask, render_template, request, url_for, flash, redirect
from matplotlib.style import use
from sqlalchemy import true
app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      return redirect(url_for("login"))
   return render_template("home.html")

@app.route('/login', methods = ['POST', 'GET'] )
def login():
   if request.method== 'POST':
      username=request.form["username"]
      print(username)
      try:
         return redirect(url_for("feedback"))
      except Exception as e:
         return redirect(url_for("login"))
   
   
   return render_template("login.html")
@app.route('/feedback')
def feedback():
   return render_template("feedbackform.html")

if __name__ == '__main__':
   app.run(debug = True)