import requests
import json
BASE_URL = "http://127.0.0.1:5000"

if __name__ == "__main__":
    for i in range(1,5):
        data_ = {"nome" : f"Teste{i}",
                 "idade" : i + 10}
        resp = requests.post(BASE_URL + "/send", data=json.dumps(data_), headers={"Content-Type" : "application/json"})
        print(resp.status_code)
      
    resp = requests.get(BASE_URL+"/data") 
    print(resp.json()) 
    
    for k in range(1,5):
        data_ = {"nome" : f"NewTeste{k}",
                 "idade" : k + 10}
        resp = requests.put(BASE_URL + f"/update/{k}", data=json.dumps(data_), headers={"Content-Type" : "application/json"})
        print(resp.status_code)
        
    resp = requests.get(BASE_URL+"/data") 
    print(resp.json()) 
     
    for j in range(1,5):
        resp = requests.delete(BASE_URL + f"/delete/{j}")
        print(resp.status_code)