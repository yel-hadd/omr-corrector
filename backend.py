from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [{
    "id": 1,
    "name": "macbook pro",
    "price": 1400
        },
        {
    "id": 2,
    "name": "ipad pro",
    "price": 800
        }]


class Item(Resource):
    def get(self, id):
        item = next(filter(lambda x: x['id'] == id, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, id):
        if next(filter(lambda x: x['id'] == id, items), None):
            return {"error": f"Item with the id {id} already exists"}, 400
        data = request.get_json(force=True)
        item = {"id": id, "name": data['name'], "price": data['price']}
        items.append(item)
        return item, 201


class Items(Resource):
    def get(self):
        return jsonify(items)


api.add_resource(Item, '/item/<int:id>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
