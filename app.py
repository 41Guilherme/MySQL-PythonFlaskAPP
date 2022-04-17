from flask import Flask, jsonify, request ,render_template
from db import DB

app = Flask(__name__)

@app.route('/help', methods=['GET'])
def help():
    return render_template("index.html")
    
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
    if (len(data) <= 0):
        DB.insertItem(1, str(New['nome']), int(New['idade']))
        return jsonify(New), 201
    id = data[index]['id'] + 1
    
    DB.insertItem(int(id), str(New['nome']), int(New['idade']))
    
    return jsonify(New), 201
    
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    DB.deleteEspecificItem(id)
    data = DB.getAllData()
    response = {"result" : data}
    return jsonify(response), 201
    
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    New = request.get_json()
    DB.updateEspecificItem(id, New['nome'], New['idade'])
    response = DB.getEspecificPerson(str(New['nome']))
    return  response , 200


if __name__ == "__main__":
    app.run(debug=True)
  
    
    
