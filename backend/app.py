from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/upload_chart', methods=['POST'])
def upload_chart():
    # Logic for uploading chart will go here
    return jsonify({'message': 'Chart uploaded successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)