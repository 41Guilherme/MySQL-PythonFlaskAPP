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
    
    
if __name__ == "__main__":
    app.run(debug=True)
  
    
    
