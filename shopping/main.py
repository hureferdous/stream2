from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
     return render_template('user.html')

@app.route('/shopping')
def shopping():
     food = ["Milk","Banana","Egg"]
     return render_template('shopping', food=food)

if __name__ == "__main__":
    app.run()