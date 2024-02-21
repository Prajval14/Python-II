from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post" action="/echo">
            <input type="text" name="text" placeholder="Enter some text" />
            <input type="submit" value="Echo" />
        </form>
    '''

@app.route('/echo', methods=['POST'])
def echo():
    user_input = request.form['text']
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)