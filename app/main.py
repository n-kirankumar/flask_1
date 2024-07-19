from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_info():
    return jsonify ({'name':'kiran','age': 24 ,'occupation': 'Developer'})

if __name__ == '__main__':
    app.run(debug = True)
