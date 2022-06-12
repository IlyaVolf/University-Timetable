from crypt import methods
from flask import Flask, jsonify, request
from flask_cors import CORS

from EntitySerializer import serialiseTeacher
from DatabaseManager import DatabaseManager

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

@app.route('/teachers/<id>', methods=['GET','DELETE','PUT'])
def teacher(id):
    response_object = {'id': 'null', 'name': 'null','daysCanWork': 'null',
    'daysWantWork': 'null', 'weight': 'null'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        teacher = dbManager.getTeacher(id)
        dbManager.close()
        response_object = serialiseTeacher(teacher)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeTeacher(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        name = request.args.get('name')
        daysCanWork = request.args.get('daysCanWork')
        daysWantWork = request.args.get('daysWantWork')
        weight = request.args.get('weight')
        if name is not None and daysCanWork is not None and daysWantWork is not None and weight is not None:
            dbManager = DatabaseManager()
            dbManager.updateTeacher(id, name, daysCanWork, daysWantWork, weight)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/teachers', methods=['POST'])
def addTeacher():
    name = request.args.get('name')
    daysCanWork = "[" + request.args.get('daysCanWork').replace(" ", ",") + "]"
    daysWantWork = "[" + request.args.get('daysWantWork').replace(" ", ",") + "]"
    weight = request.args.get('weight')
    if name is not None and daysCanWork is not None and daysWantWork is not None and weight is not None:
        dbManager = DatabaseManager()
        dbManager.addTeacher(name, daysCanWork, daysWantWork, int(weight))
        dbManager.close()
        return jsonify({'response': 'success'})
    return jsonify({'response': 'failure'})

if __name__ == '__main__':
    app.run()