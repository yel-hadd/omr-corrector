from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'randomsecretkey'
api = Api(app)
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="this field cannot be left blank")
    parser.add_argument("price", type=float, required=True, help="this field cannot be left blank")
    @jwt_required()
    def get(self, id):
        item = next(filter(lambda x: x['id'] == id, items), None)
        return {'item': item}, 200 if item else 404

    @jwt_required()
    def post(self, id):
        global items
        if next(filter(lambda x: x['id'] == id, items), None):
            return {"error": f"Item with the id {id} already exists"}, 400
        data = Item.parser.parse_args()
        item = {"id": id, "name": data['name'], "price": data['price']}
        items.append(item)
        return item, 201

    @jwt_required()
    def delete(self, id):
        global items
        items = list(filter(lambda x: x['id'] != id, items))
        return {"message": f"Item {id} has been deleted"}, 401

    @jwt_required()
    def put(self, id):
        global items
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['id'] == id, items), None)
        if item == None:
            item = {"id": id, "name": data["name"], "price": data["price"]}
            items.append(item)
            return f"a new item with id {id} has been created", 201
        else:
            item.update(data)
            return f"Item {id} has been updated", 201

class Items(Resource):
    @jwt_required()
    def get(self):
        return jsonify(items)


api.add_resource(Item, '/item/<int:id>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
