import json, falcon


class ObjRequestClass:

    __json_content = {}

    def __validate_json_input(self, request):
        try:
            self.__json_content = json.loads(request.stream.read())
            print("Json content is ok")
            return True
        except:
            self.__json_content = {}
            print("Json content is NOT OK")
            return False

    def on_get(self, request, resp):
        resp.status = falcon.HTTP_200
        validate = self.__validate_json_input(request)

        output = {
            "status" : 200,
            "msg" : None,
            "username" : "SomeBloke",
            "name" : "Janusz"
        }
        if validate:

            output["msg"] = "Hello {}".format(self.__json_content["name"])
            if output['username'] == 'SomeBloke':
                output['value'] = output['name']
            else:
                resp.status = falcon.HTTP_404
                output['value'] = None
        else:
            output["status"] = 404
            output["msg"] = "Json  input is not valid"
            if 'username' not in output:
                resp.status = falcon.HTTP_501
                output['value'] = 'Error: username not in data'

        resp.body = json.dumps(output)

    def on_post(self, request, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(request.stream.read())
        equal = int(data['x']) + int(data['y'])
        output = {
            'count' : 'x: {} + y: {}  is equal to {}'.format(str(data['x']), str(data['y']), str(equal))
        }
        resp.body = json.dumps(output)

    def on_put(self, request, resp):
        resp.status = falcon.HTTP_200
        output = {
            "msg" : "Put method is project in progress"
        }
        resp.body = json.dumps(output)

    def on_delete(self, request, resp):
        resp.status = falcon.HTTP_200
        output = {
            "msg": "Delete method is project in progress"
        }
        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/test', ObjRequestClass())