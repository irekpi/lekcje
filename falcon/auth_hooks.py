import falcon


class Authorize:
    def __init__(self, roles):
        self._roles = roles

    def __call__(self, request, resp, resource, params):
        if 'Admin' in self._roles:
            request.user_id = 5
        else:
            raise falcon.HTTPBadRequest('Bad request', "Your  are not admin")


class ObjectResource:

    @falcon.before(Authorize(['Admin', 'Normal', "Basic"]))
    def on_get(self, request, resp):
        print("trigger - Get")
        output = {
            "method" : 'get',
            "user-id" : request.user_id
        }
        resp.media = output

    @falcon.before(Authorize(['Normal', "Basic"]))
    def on_post(self, request, resp):
        print("trigger - Post")
        output = {
            "method" : 'post',
            "user-id" : request.user_id
        }
        resp.media = output


api = falcon.API()
api.add_route('/auth_hooks', ObjectResource())
