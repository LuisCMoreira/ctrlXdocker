from flask import Flask, jsonify, request, render_template
import ctrlXapi as ctX

app = Flask(__name__)

# ctrlX parameters
address = "localhost"
user = "boschrexroth"
password = "boschrexroth"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/paths', methods=['GET'])
def get_paths():
    try:
        token = ctX.get_token(address, user, password)
        vGroup = "plc/app/Application/sym/"
        available_data = ctX.browse_data(address, token, vGroup)
        return jsonify(available_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/write', methods=['POST'])
def write_value():
    try:
        token = ctX.get_token(address, user, password)
        data = request.json
        path = data.get('path')
        value = data.get('value')
        data_type = data.get('type')  # e.g., "bool8", "string"

        if not path or value is None or not data_type:
            return jsonify({"error": "Path, value, and type are required"}), 400

        ctX.set_value(address, token, path, data_type, value)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
