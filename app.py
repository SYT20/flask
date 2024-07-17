from flask import Flask,url_for
from flask import request
app = Flask(__name__)

@app.route("/hey")
def hello_world():
    return "<h1>Hello, World!</h1>"
@app.route("/test")
def test():
    try:
        data1 = int(request.args.get('num1'))
        data2 = int(request.args.get('num2'))
    except ValueError:
         return "Invalid input. Please provide integer values for num1 and num2."
    else:
        return f"Sum of the {data1} and {data2} is: {data1+data2}"

@app.route("/test1/<num1>")
def test1(num1):
    try:
        num = int(num1)
    except ValueError:
        return "Invalid input. Please provide an integer."
    return f"The input is {num}"

@app.route("/greet/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/")
def index():
    # Generate URL for the hello function
    hello_url = url_for('hello', name='Alice')
    return f"Visit {hello_url} to greet Alice."


@app.route('/search')
def search():
    query = request.args.get('q')
    return f"You searched for: {query}"

@app.route('/')
def index():
    search_url = url_for('search', q='Flask tutorials')
    return f"Search for Flask tutorials here: {search_url}"

@app.route('/hey/path')
def test():
    return "testing for path using url_for"
@app.route('/')
def test1():
    test_url = url_for('test')
    return f"To visit test function use url = {test_url}"

@app.route('/hey/<path>')
def hello(path):
    return f"the input path is {path}"
@app.route('/')
def test():
    try:
        var = request.args.get('x')
    except ValueError:
        return "Value error occured"
    else:
        test_url = url_for('hello',path = var)
        return f"the url to visit test function is: {test_url}"

if __name__=="__main__":
    app.run(host="0.0.0.0")
