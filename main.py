## main python file

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from stocks import query_api
app = Flask(__name__)
@app.route('/')

def index():
    return render_template(
        'stock.html',
        data=[
        {'name':'Tesla'}, 
        {'name':'Apple'}, 
        {'name':'Google'},
        {'name':'Intuit'},
        {'name':'Goldman Sachs'}, 
        {'name':'Microsoft'},
        {'name':'Bitcoin'},
        {'name':'Dogecoin'}])

@app.route("/result" , methods=['GET', 'POST'])

def result():
    tickerDict = {'Tesla': "TSLA", 'Apple': "AAPL", 'Google' : "GOOG", 'Microsoft': "MSFT",'Samsung': "SSNLF", "Intuit": 'INTU', "Goldman Sachs": 'GS','Dogecoin': "DOGE-USD", 'Bitcoin': 'BTC-USD'}
    data = []
    error = None
    select = request.form.get('comp_select')
    print(select)
    company_select = ''
    for cursor in tickerDict.keys():
        if cursor == select:
            company_select = tickerDict[cursor]
            print(company_select)
            if company_select == 'BTC-USD' or company_select == 'DOGE-USD':
                resp = query_api(company_select)
                if resp:
                    data.append(resp)
                return render_template(
                'result_crypto.html',
                data=data)
                
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