import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'] )
def home():
        return"<h1>this is a python server</h1>"

app.run()