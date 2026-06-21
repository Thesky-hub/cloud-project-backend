from flask import Flask
import redis
import os

app = Flask(__name__)
# 连接 Redis
r = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=int(os.environ.get('REDIS_PORT', 6379)))

@app.route('/api/ping')
def ping():
    return {"status": "ok", "message": "Backend received request!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)