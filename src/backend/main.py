from flask import Flask, jsonify
import redis
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

def init_db():
    redis_host = os.getenv('REDIS_HOST', 'redis')
    redis_port = os.getenv('REDIS_PORT', '6379')
    r = redis.Redis(host=redis_host, port=redis_port)
    r.rpush('list', 'item1', 'item2', 'item3') 


def get_db_results():
    redis_host = os.getenv('REDIS_HOST', 'redis')
    redis_port = os.getenv('REDIS_PORT', '6379')
    r = redis.Redis(host=redis_host, port=redis_port)
    results = r.lrange('list', 0, -1)
    return [str(item) for item in results]

@app.route('/api/results', methods=['GET'])
def results():
    data = get_db_results()
    return jsonify(data)

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='0.0.0.0', port=5001)