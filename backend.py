from flask import Flask, jsonify, request, render_template
import cv2
import main

app = Flask(__name__)

stores = [
    {
        "name": "YASSINE",
        "items": [
            {
                "name": "My Item",
                "price": 15.99
            }
        ]
    }
]

@app.route("/")
def home():
    return 'Hello WRLD'

# POST /store data
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return store
    return jsonify({"message": "ERROR STORE NOT FOUND"})

# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})
    

# POST /store/<string:name>/item
@app.route("/store/<string:name>/item", methods=["POST"])
def post_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
                }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"error": "store not found"})
    
# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({"message": "ERROR ITEM NOT FOUND"})

app.run(port=5000)