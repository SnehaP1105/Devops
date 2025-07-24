from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask API!"

@app.route('/health')
def health():
    return jsonify(status="healthy")

@app.route('/api/users')
def users():
    return jsonify(users=["Alice", "Bob", "Charlie"])

@app.route('/api/info')
def info():
    return jsonify(app="Mini Project API", version="1.0")

if __name__ == '__main__':
    app.run(debug=True)
