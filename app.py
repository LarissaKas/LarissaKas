from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(message="Привет из API!", data=[1, 2, 3])

@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.json
    name = data.get('name', 'Гость')
    return jsonify(message=f'Привет, {name}!')

if __name__ == '__main__':
    print("Запуск приложения...")
    app.run(host='0.0.0.0', port=5000)
