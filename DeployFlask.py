from flask import Flask 

app = Flask(__name__)

# load model 
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