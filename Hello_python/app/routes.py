from app import app 
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
     user=[
          {'id':'id01','name':'A'},
          {'id':'id02','name':'B'},
          {'id':'id03','name':'C'}
          ]

     return render_template('index.html',title="My title",user=user)