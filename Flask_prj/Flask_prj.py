from flask import Flask, abort
from flask import render_template  # Add this as the last import at the beginning of the file
app = Flask(__name__)

ages = {
    'bob': '43',
    'alice': '29'
}


@app.route('/users/<user>')
def users(user):
    age = ages.get(user)
    return render_template('user.html', user=user, age=age)


@app.route('/customer/<user>')
def customer(user):
    age = ages.get(user)
    if age:
        return '%s is %s years old' % (user, age)
    else:
        abort(404)


@app.route('/')
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)