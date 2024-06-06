from flask import Flask, render_template,request
app = Flask (__name__)

@app.route ('/', methods=["POST", "GET"])
def calc():

    if request.method =="POST":

        n1 = float (request.form["num1"])
        n2 = float (request.form["num2"])
        Operations = request.form["Operations"]

        if Operations == '+':
             result = n1+n2

        elif Operations == '-':
            result = n1-n2

        elif Operations == '*':
            result = n1*n2

        elif Operations == '/':
            result = n1/n2
        
        else:
            result = "Invalid Data Entered"
        return render_template('calculator.html', result = result)
    else:
        return render_template('calculator.html')

#hello

app.run(debug=True)
