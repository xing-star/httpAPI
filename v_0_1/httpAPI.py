from flask.views import MethodView



class HttpAPI(MethodView):

    def get(self):
        return 'get function '

    def post(self):
        return 'post function '

    def put(self):
        return 'put function '

    def delete(self):
        return 'delete function '
