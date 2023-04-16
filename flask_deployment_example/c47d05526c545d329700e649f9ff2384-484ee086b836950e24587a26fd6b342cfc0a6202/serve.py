from flask import Flask

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
    
     classifier = joblib.load('classifier.pkl')
     prediction = classifier.predict(query)
     return jsonify({'prediction': list(prediction)})


if __name__ == '__main__':
     app.run(port=8080)