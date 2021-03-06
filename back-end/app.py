import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS,cross_origin

## Init app
app = Flask(__name__)

## Connect DB

client = MongoClient('localhost', 27017)
db = client.discoverer
collection = db.tools

## CORS
CORS(app,resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

## routes
@app.route('/api/get_tool', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def get_message():
    try:
        tool_name = request.args.get('tool_name')
        entry = collection.find_one({'name' : tool_name})
        data = { 'name' : tool_name, 'description' : entry['description'][0]}
    except Exception as err:
        data = {'message': err, 'code': 'ERROR'}
        resp = make_response(data, 400)
        print(err)
    else:
        data = {'message': data, 'code': 'SUCCESS'}
        resp = make_response(jsonify(data), 201)
    finally:
        resp.set_cookie('same-site-cookie', 'foo', samesite='Lax')
        resp.set_cookie('cross-site-cookie', 'bar', samesite='Lax', secure=True)
        return resp

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
