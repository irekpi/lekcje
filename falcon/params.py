import json, falcon


class ObjRequestClass:
    def on_get(self, request, resp):
        resp.status = falcon.HTTP_200

        validate = False
        if 'name' and 'age' in request.params:
            validate = True

        if validate:
            output = {
                "name" : request.params['name'],
                "age" : request.params['age']
            }
        else:
            output = {
                "error" : "Not all info is provided"
            }

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/params', ObjRequestClass())