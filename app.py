from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/predict",methods=['POST'])
def predict():
    x = request.json['x']
    x = np.array(x).reshape(-1,1)
    y = model.predict(x).tolist()
    return jsonify({"y":y})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5002)