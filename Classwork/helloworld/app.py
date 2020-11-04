from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello, world!"

# @app.route('/profile/<users_name>')
# def profile(users_name):
#     return "Hello " + users_name

@app.route('/triple/<word>')
def triple(word):
    return word*3

if __name__ == '__main__':
    app.run(debug=True)
