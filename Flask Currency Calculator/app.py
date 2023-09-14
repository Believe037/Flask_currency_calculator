from flask import Flask, render_template, request, redirect, url_for

import re

app = Flask(__name__)



@app.route("/", methods=['GET','POST'])
def home():
      r = re.compile(r"^(\d+|\d{1,3}(,\d{3})*)(\.\d+)?$")
      number1 = ""
      currency = ""
      if request.method == 'POST':
        number1 = request.form['num1']
        currency = request.form['currency']

      num1 = number1.replace(",", "")
      num1 = num1.replace(".", "")
      print(num1)
      
      if not r.match(num1):
        result = 0
        value = ""
        content = ""
        textBody1 = "Sorry you must input a valid NGN."
        textBody2 = ""
      elif currency == "":
        result = 0
        value = ""
        content = ""
        textBody1 = "Sorry you must choose a currency"
        textBody2 = ""
          
      else:
        textBody1 = "The value in "
        textBody2 = "is: "
        num1 = number1.replace(",", "")
        num1 = float(num1)
        result = 0
        if currency == 'usd':
          result = num1 / 777.50
          content = 'USD'
          value = "$"
        elif currency == 'euro':
          result = num1 / 833.50
          content = 'EURO'
          value = "€"
        elif currency == 'gbp':
          result = num1 / 970.09
          content = 'GBP'
          value = "£"

      if result == 0:
        result = ""
      else:
        result = "{:,.3f}".format(result)

      return render_template('index.html', result=result, currency=currency, num1=num1, textBody1=textBody1, textBody2=textBody2, value=value, content=content)



if __name__ == "__main__":
  app.run(debug=True)