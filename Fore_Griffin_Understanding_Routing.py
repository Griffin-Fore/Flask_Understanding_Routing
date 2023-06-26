from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_hi(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/<int:number>/<string:word>')
def count_word(number,word):
    return word * number


if __name__=="__main__":
    app.run(debug=True)