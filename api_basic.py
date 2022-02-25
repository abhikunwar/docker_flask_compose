from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app = Flask("__name__")
api = Api(app)

def varify_value(dict_data):
    if len(dict_data) !=2:
        return 301

class Add(Resource):
    def post(self):
        # get the data
        json_data = request.get_json()
        st_code = varify_value(json_data)
        if st_code != 301:
            x = json_data['first_data']
            y = json_data['second_data']
            x = int(x)
            y = int(y)
            # manupulate the data
            ret = x + y
            out = {
                "result": ret,
                "response_code":200
            }
            # return jason responce
            return jsonify(out)
        else:

            out = {
                "result": "please enter two values",
                "response_code":301
                } 
            return jsonify(out)  
    def get():
        pass
# adding path to the resource
api.add_resource(Add,'/addition')

if __name__=="__main__":
    app.run(host='0.0.0.0')    


