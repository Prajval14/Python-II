from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post" action="/calculate">
            <input type="number" name="num1" placeholder="Enter number 1" />
            <input type="number" name="num2" placeholder="Enter number 2" />
            </br></br>
            <input type="submit" value="Add" name="operation" />
            <input type="submit" value="Subtract" name="operation" />
            <input type="submit" value="Multiply" name="operation" />
            <input type="submit" value="Divide" name="operation" />
        </form>
    '''

@app.route('/calculate', methods=['POST'])
def echo():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation_type = request.form['operation']
    if operation_type == 'Add':
        result = num1 + num2
    elif operation_type == 'Subtract':
        result = num1 - num2
    elif operation_type == 'Multiply':
        result = num1 * num2
    else:
        result = num1 / num2
    return f"Result: {result}"

@app.route('/template', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)