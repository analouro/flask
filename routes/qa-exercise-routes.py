from flask import Flask

app = Flask(__name__)

@app.route('/home/<number>')
def home(number):
    number = int(number) # We need to convert 'number' as a int to make a calculation because in the URL it comes as a string
    final_number = number*number
    return str(final_number) # We need to return the answer as a string because URL doesn't accept int 

# OR

# @app.route('/home/<int:number>')
# def home2(number):
# return str(number ** 2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)