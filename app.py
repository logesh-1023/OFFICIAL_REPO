from flask import Flask 

app = Flask('__name__')

@app.route('/')
def home():
    return "This is a Test App ran by Local System by Logesh & Commit System and This is Trial 2"

if __name__ == '__main__':
    app.run(debug=False,port=6060)