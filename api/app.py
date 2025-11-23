from flask import Flask, request, jsonify
from flask_cors import CORS
datas={'yogesh':327647234,'faf':734634734,'shankar':664569345,'pradeep':87576346,'sachin':373273263}

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask API with CORS is running!"})

@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.get_json()

    name = data.get("name")
    
    
  
    for key,value in datas.items():
            if name==key:
                print(key)
                return jsonify({
                    'status':'success',
                    'message':f'hello this is your id {value} bro'
                })


    print(name)
    return jsonify({
        "status": "success",
        "message": f" what bro you are  wrong bro !!!!"
    })

if __name__ == "__main__":
    app.run(debug=True)
