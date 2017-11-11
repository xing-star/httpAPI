from flask.views import MethodView
from flask import render_template, jsonify


class HttpAPI(MethodView):

    def get(self):
        getStr = {'function': 'getFunction'}
        return 'get function'

    def post(self):
        return 'post function'

    def put(self):
        return 'put function'

    def delete(self):
        return 'delete function'


class Index(MethodView):

    def get(self):
        return render_template('index.html')
