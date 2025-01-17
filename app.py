from flask import Flask 

app = Flask('__name__')

@app.route('/')
def home():
    return "This is a Test App ran by Local System by Mani 17/01/2025"

if __name__ == '__main__':
    app.run(debug=False,port=6060)