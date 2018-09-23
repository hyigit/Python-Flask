from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', number1 = 10, number2 = 20)

@app.route('/hello')
def hello_world():
  return 'Hello, Alp!'

@app.route('/search')
def search():
  return 'Search Page'

@app.route('/delete/<string:id>')
def deleteId(id):
  return 'Id: ' + id

if __name__ == '__main__':
  app.run(debug=True)



