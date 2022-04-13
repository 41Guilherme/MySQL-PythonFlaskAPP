from flask import Flask, jsonify, request 
from db import DB

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = DB.getAllData()
    response = {
        "result" : data
    }
    return jsonify(response) ,200


@app.route('/send', methods=['POST'])
def send_user():
    New = request.get_json()
    data = DB.getAllData()
    index = len(data) -1
    id = data[index]['id'] + 1
    
    DB.insertItem(int(id), str(New['nome']), int(New['idade']))
    
    return jsonify(New), 200
    
    
if __name__ == "__main__":
    app.run(debug=True)
  
    
    
