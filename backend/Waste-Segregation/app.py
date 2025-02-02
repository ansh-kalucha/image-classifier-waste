from flask import Flask, request, jsonify, render_template
from model import get_output
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<center><h1>Hello Welcome to Waste Segregation!!</h1></br><h2>This is Backend site</h2></center>"

@app.route('/predict', methods=['POST'])
def predict():
    path = request.get_json(force=True)
    url = path['image']
    print(url)   
    prediction = get_output(url) 
    print(prediction)
    data = {'predict': prediction}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
