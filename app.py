from http.client import HTTPException
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import json
import time
from flask import Response, stream_with_context


with open('zx_example.json', 'r') as f:
    zx_example = json.load(f)

with open('wd_example.json', 'r') as f:
    wd_example = json.load(f)

JWT_SECRET_KEY = 'NJUCM'
USERNAME = 'njucm'
PASSWORD = 'njucm'

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
jwt = JWTManager(app)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(Exception)
def handle_exception(e):
    print(e)
    if isinstance(e, HTTPException):
        return e
    return jsonify(error="Internal Server Error"), 500

@app.route('/')
def index():
    return jsonify({'message': 'success!'})

@app.route('/auth', methods=['POST'])
def auth():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != USERNAME or password != PASSWORD:
        return jsonify({"msg": "Bad username or password"}), 401
    expires = timedelta(days=30)
    access_token = create_access_token(identity=username, expires_delta=expires)
    print(access_token)
    return jsonify(access_token=access_token)

@app.route('/api/v1/wd', methods=['POST'])
@jwt_required()
def wd():
    question = request.json.get('question', None)
    def generate():
        try:
            for i in range(500):
                time.sleep(1)
                data = json.dumps(wd_example)
                yield f"data: {data}\n\n"
                time.sleep(1)
        except GeneratorExit:
            print("客户端断开连接！")
    return Response(stream_with_context(generate()), content_type='text/event-stream')

@app.route('/api/v1/zx', methods=['POST'])
@jwt_required()
def kyzx():
    name = request.json.get('name', None)
    gender = request.json.get('gender', None)
    age = request.json.get('age', None)
    disease = request.json.get('disease', None)
    question = request.json.get('question', None)
    return jsonify(zx_example)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
