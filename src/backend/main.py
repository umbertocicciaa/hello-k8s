from flask import Flask, jsonify
import redis
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

def init_db():
    r = redis.Redis(host='db', port=6379, decode_responses=True)
    r.rpush('your_list', 'item1', 'item2', 'item3')

def get_db_results():
    r = redis.Redis(host='db', port=6379, decode_responses=True)
    results = r.lrange('your_list', 0, -1)
    return results

@app.route('/api/results', methods=['GET'])
def results():
    data = get_db_results()
    return jsonify(data)

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='0.0.0.0', port=5001)