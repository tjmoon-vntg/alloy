from flask import Flask
from prometheus_client import start_http_server, Counter
import time
import random

app = Flask(__name__)

# 메트릭 정의: 'http_requests_total' 라는 이름의 Counter
REQUESTS = Counter('http_requests_total', 'Total HTTP requests received', ['endpoint'])

@app.route('/')
def hello():
    # '/' 엔드포인트가 호출될 때마다 카운터 증가
    REQUESTS.labels(endpoint='/').inc()
    return "Hello! Metrics are available at /metrics"

@app.route('/test')
def test():
    # '/test' 엔드포인트가 호출될 때마다 카운터 증가
    REQUESTS.labels(endpoint='/test').inc()
    return "Test page!"

if __name__ == '__main__':
    # 8000번 포트에서 /metrics 엔드포인트 시작
    start_http_server(8000)
    # 8080번 포트에서 Flask 앱 실행 (컨테이너 내부)
    app.run(host='0.0.0.0', port=8080)
