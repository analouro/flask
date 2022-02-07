from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet - Ana has arrived!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# ACCESS THE WEB APP: http://localhost:5000/
# TO STOP THE WEB APP FROM RUNNING: Press CTRL+C in Terminal