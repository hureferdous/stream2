from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    return "method used is: %s" % request.method

@app.route("/bacon", method=['GET','POSt'])
def bacon():
     if request.method == 'POST':
        return 'You used POST'
     else:
        return 'you used GET'

if __name__ == "__main__":
    app.run()

