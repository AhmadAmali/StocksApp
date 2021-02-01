## main python file

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from stocks import query_api
app = Flask(__name__)
@app.route('/')

def index():
    return render_template(
        'stock.html',
        data=[{'name':'Tesla'}, {'name':'Apple'}, {'name':'Google'},
        {'name':'Samsung'},{'name':'Intuit'},
        {'name':'Goldman Sachs'}, {'name':'Microsoft'}])

@app.route("/result" , methods=['GET', 'POST'])

def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Stocks API'
    return render_template(
        'result.html',
        data=data,
        error=error)

if __name__=='__main__':
    app.run(debug=True)