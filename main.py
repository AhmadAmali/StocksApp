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
    tickerDict = {'Tesla': "TSLA", 'Apple': "AAPL", 'Google' : "GOOG", 'Microsoft': "MSFT",'Samsung': "SSNLF", "Intuit": 'INTU', "Goldman Sachs": 'GS'}
    data = []
    error = None
    select = request.form.get('comp_select')
    print(select)
    company_select = ''
    for cursor in tickerDict.keys():
        if cursor == select:
            company_select = tickerDict[cursor]
    resp = query_api(company_select)
    if resp:
       data.append(resp)
    else:
        error = 'Bad Response from Stocks API'
    pp(data)
    return render_template(
        'result.html',
        name=select,
        data=data,
        error=error)

if __name__=='__main__':
    app.run(debug=True)