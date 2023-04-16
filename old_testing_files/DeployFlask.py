from flask import Flask, render_template, request

app = Flask(__name__)

# https://www.youtube.com/watch?v=2LqrfEzuIMk
# load model 
# model = .load('')

# Home page
@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # input features 
    # wineFeatures = request.form['wineFeatures']
        # might need to convert to float?
    # wineFeatures = float(request.form['wineFeatures'])
    # continue with other inputs 
        # results will be an array, index of [0]
    # result = model.predict([[feature1, feature2, feature3]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)


# route to take user input
# pass input to model (preprocessing)
# return predicted output

# Need some kind of insurance if user input is way of of range (too large or negative)

# @app.route("/")
# def predict(input_user:str):
#     print('test-predict')
#     return input_user

# if __name__ == "__main__":
#     app.run(debug=True)