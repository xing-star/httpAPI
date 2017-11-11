from flask import Flask
from httpAPI import HttpAPI, Index

app = Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=['GET','POST','PUT','DELETE'])
app.add_url_rule('/httpAPI', view_func=HttpAPI.as_view('httpAPI'), methods=['GET','POST','PUT','DELETE'])

if __name__ == "__main__":
    app.run()
