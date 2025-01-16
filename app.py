from flask import Flask 

app = Flask(__main__)

@app.route('/')
def home():
    return "This is A"

if __main__ == '__name__':
    app.run(debug=False,port=6060)