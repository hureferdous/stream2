from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Hure, Are You Here'

@app.route('/tinua')
def tinua():
    return '<h2>She is a good girl</h2>'


@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hye there is %s </h2>'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h2>Post ID is %s </h2>'%post_id



if __name__ == "__main__":
    app.run(debug=True)