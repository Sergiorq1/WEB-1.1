from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello, world!"

@app.route('/profile/<users_name>')
def profile(users_name):
    return "Hello " + users_name
    
if __name__ == '__main__':
    app.run(debug=True)
