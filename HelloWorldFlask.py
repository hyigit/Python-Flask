from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, Alp!'

@app.route('/search')
def search():
  return 'Search Page'

@app.route('/delete/<string:id>')
def deleteId(id):
  return 'Id: ' + id

app.run(host='0.0.0.0', port=8080)

