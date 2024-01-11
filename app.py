import json
from random import randint

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

products = dict()
products[0] = {'name': 'banana', 'file': 'banana.jpg'}

@app.route('/all', methods=['GET'])
def get_all_products():
    return products

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    if request.method == 'GET':
        id = request.args.get('id')
        if id:
            return send_file(products[int(id)]['file'])
            # return products[int(id)]
        else:
            return jsonify(products)
    if request.method == 'POST':
        name = request.args.get('name')
        id = len(products)
        products[id] = {'name': name}
        return 'ID of added product: ' + str(id)
    if request.method == 'PUT':
        id = request.args.get('id')
        name = request.args.get('name')
        if id and int(id) in products.keys():
            products[int(id)] = name
            return "SUCCESS"
        else:
            return "WRONG ID"
    if request.method == 'DELETE':
        id = request.args.get('id')
        if id and int(id) in products.keys():
            del products[int(id)]
            return "SUCCESS"
        else:
            return "WRONG ID"


if __name__ == '__main__':
    app.run()
