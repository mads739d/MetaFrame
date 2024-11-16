from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to MyCoolApp!'

if __name__ == '__main__':
    app.run(debug=True)
