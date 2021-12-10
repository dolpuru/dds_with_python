#리턴 데이터를 json포멧으로 구현
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/json_test")
def hello_json():
    data = {'name' : '김명준', 'family' : 'ys'}
    return jsonify(data)
@app.route('.server_info')
def server_json():
    data = {'server_name': '0.0.0.0','server_port':'8000'}
    return jsonify(data)
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = '8080')
    