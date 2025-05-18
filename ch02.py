from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    content = request.json
    return jsonify({"received": content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)