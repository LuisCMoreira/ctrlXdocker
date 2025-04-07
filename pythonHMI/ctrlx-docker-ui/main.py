from flask import Flask, jsonify, render_template, request
import ctrlXapi as ctX

app = Flask(__name__)

# ctrlX parameters
address = "192.168.1.1"
user = "boschrexroth"
password = "boschrexroth"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/browse', methods=['GET'])
def browse_data():
    try:
        token = ctX.get_token(address, user, password)
        vGroup = "plc/app/Application/sym/GVL_customHMI/"
        available_data = browse_recursive(address, token, vGroup)
        return jsonify(available_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def browse_recursive(address, token, path):
    """Recursively browse the data paths and return a flat list of paths and types."""
    data = ctX.browse_data(address, token, path)
    paths_and_types = []
    data_values = {}
    for variable in data.get('value', []):
        data_value = ctX.get_value(address, token, path + variable)
        data_values[variable] = data_value
        paths_and_types.append({"path": path + variable, "type": data_values[variable]['type'], "value": data_values[variable]['value']})
    return paths_and_types

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

        # Convert value to the appropriate type
        if data_type == "bool8":
            value = value.lower() == 'true'
        
        # Convert value to the appropriate type
        if data_type == "double":
            value = float(value)

        print( data_type)
        ctX.set_value(address, token, path, data_type, value)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
