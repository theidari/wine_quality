import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# from pathlib import Path

# Load model file for white
# filename = Path('LogRDummyModel.pkl')
# model_white = pickle.load(open('Resources/LogRDummyModelWhite.pkl', 'rb'))
model_white = pickle.load(open('Resources/svm_model_white.pkl', 'rb'))
# Load model file for red
model_red = pickle.load(open('Resources/svm_model_red.pkl', 'rb'))

# Load and scale datasets, in order to scale new data coming in
df_white = pd.read_csv('Resources/white_train_norm.csv', sep = ',')
df_red = pd.read_csv('Resources/red_train_norm.csv', sep = ',')

X_white = df_white.drop(columns = ['quality', 'total sulfur dioxide',
                                     'density', 'citric acid', 'residual sugar'])
X_red = df_red.drop(columns=['quality', 'total sulfur dioxide',
                                     'density', 'citric acid', 'residual sugar'])

scaler_white = StandardScaler()
scaler_red = StandardScaler()

# Don't need to record the scaled data? Just prepare the scaler 
# or use .transform instead of .fit?
scaler_white.fit(X_white)
scaler_red.fit(X_red)

# Function to predict from model 
def predict(user_input):

    
    # if colour == 'White':
        
    #     model = model_white
    # elif colour == 'Red': 
        
    #     model = model_red 
    
    # Convert input to a dataframe to pass to .predict method
    input = pd.DataFrame(user_input_scaled,\
                         columns=['fixed acidity','volatile acidity','chlorides','free sulfur dioxide', \
                                   'pH', 'sulphates', 'alcohol']) # str(num) for num in num_list?
    # ['Fixed Acidity','Volatile Acidity','Citric Acid','Residual Sugar','Chlorides','Free Sulfur Dioxide', 'Total Sulfur Dioxide', 'Density', 'pH Level', 'Sulphates Content', 'Alcohol Content']
    prediction = model.predict(input)
    return prediction

st.title('Wine Quality Prediction')
# st.image('https://images.unsplash.com/photo-1585553616435-2dc0a54e271d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8d2luZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60')
st.header('Trained with wine data from Vinho Verde - Portugal')
st.header('Enter wine chemistry below')

tab1, tab2 = st.tabs(['White Wine', 'Red Wine'])

with tab1:
    # User feature input
    feature1 = st.number_input('Fixed Acidity', min_value = 1.5, max_value = 2.5, value=2.0, key = 'white FA')
    feature2 = st.number_input('Volatile Acidity', min_value = 0.35, max_value = 1.15, value=0.5, key = 'white VA')
    # feature3 = st.number_input('Citric Acid', min_value = 0.0, max_value = 0.95, value=0.0)
    # feature4 = st.number_input('Residual Sugar', min_value = 0.8, max_value = 3.0, value=1.0)
    feature5 = st.number_input('Chlorides', min_value = 0.2, max_value = 0.53, value=0.3, key = 'white C')
    feature6 = st.number_input('Free Sulfur Dioxide', min_value = 1.44, max_value = 4.8, value=2.5, key = 'white FSD')
    # feature7 = st.number_input('Total Sulfur Dioxide', min_value = 1.8, max_value = 259.0, value=5.0) # This one huge different b/w white and red, trying min/max of each
    # feature8 = st.number_input('Density', min_value = 0.996, max_value = 1.001, value=0.997)
    feature9 = st.number_input('pH Level', min_value = 2.72, max_value = 3.9, value=3.2, key = 'white pH')
    feature10 = st.number_input('Sulphates Content', min_value = 0.6, max_value = 1.07, value=0.8, key = 'white SC')
    feature11 = st.number_input('Alcohol Content', min_value = 8.0, max_value = 14.9, value=10.0, key = 'white AC')

    if st.button('Predict Quality', key = 'white button'):

        # Collect user input
        user_input = [feature1, feature2, feature5, feature6, feature9, feature10, feature11]
        # Scale user input to pass to model, choosing appropriate model from wine colour
        user_input_scaled = scaler_white.transform([user_input])
        model = model_white 
        # st.write(user_input_scaled)
        input = pd.DataFrame(user_input_scaled,\
                         columns=['fixed acidity','volatile acidity','chlorides','free sulfur dioxide', \
                                   'pH', 'sulphates', 'alcohol']) # str(num) for num in num_list?
        # ['Fixed Acidity','Volatile Acidity','Citric Acid','Residual Sugar','Chlorides','Free Sulfur Dioxide', 'Total Sulfur Dioxide', 'Density', 'pH Level', 'Sulphates Content', 'Alcohol Content']
    
        quality = model.predict(input)
        # quality = predict(user_input)
        if quality == 0:
            quality = 'Bad'
        if quality == 1:
            quality = 'Delicious!'
        # quality = predict(feature1, feature2, feature3) # this will just be good/bad/declious?
        st.success(f'The predicted wine quality is {quality}') # or we predict your wine to be [...]?

with tab2: 
    # User feature input
    # feature1 = st.number_input('Fixed Acidity', min_value = 1.5, max_value = 2.5, value=2.0)
    feature2 = st.number_input('Volatile Acidity', min_value = 0.35, max_value = 1.15, value=0.5, key = 'red VA')
    feature3 = st.number_input('Citric Acid', min_value = 0.0, max_value = 0.95, value=0.0, key = 'red CA')
    feature4 = st.number_input('Residual Sugar', min_value = 0.8, max_value = 3.0, value=1.0, key = 'red RS')
    feature5 = st.number_input('Chlorides', min_value = 0.2, max_value = 0.53, value=0.3, key = 'red C')
    # feature6 = st.number_input('Free Sulfur Dioxide', min_value = 1.44, max_value = 4.8, value=2.5)
    # feature7 = st.number_input('Total Sulfur Dioxide', min_value = 1.8, max_value = 259.0, value=5.0) # This one huge different b/w white and red, trying min/max of each
    # feature8 = st.number_input('Density', min_value = 0.996, max_value = 1.001, value=0.997)
    feature9 = st.number_input('pH Level', min_value = 2.72, max_value = 3.9, value=3.2, key = 'red pH')
    feature10 = st.number_input('Sulphates Content', min_value = 0.6, max_value = 1.07, value=0.8, key = 'red SC')
    feature11 = st.number_input('Alcohol Content', min_value = 8.0, max_value = 14.9, value=10.0, key = 'red AC')

    if st.button('Predict Quality', key = 'red button'):

        # Collect user input
        user_input = [feature2, feature3, feature4, feature5, feature9, feature10, feature11]
        # Scale user input to pass to model, choosing appropriate model from wine colour
        user_input_scaled = scaler_red.transform([user_input])
        model = model_red

        input = pd.DataFrame(user_input_scaled,\
                         columns=['volatile acidity','citric acid', 'residual sugar','chlorides', \
                                   'pH', 'sulphates', 'alcohol'])
        
        quality = model.predict(input)
        if quality == 0:
            quality = 'Bad'
        if quality == 1:
            quality = 'Delicious!'
        # quality = predict(feature1, feature2, feature3) # this will just be good/bad/declious?
        st.success(f'The predicted wine quality is {quality}') # or we predict your wine to be [...]?

# colour = st.selectbox('Red or White:', ['Red','White'])

# Calls the predict function from user input on button press
# if st.button('Predict Quality'):

#     # Collect user input
#     user_input = [feature1, feature2, feature5, feature6, feature9, feature10, feature11]
    
#     quality = predict(user_input)
#     if quality == 0:
#         quality = 'Bad'
#     if quality == 1:
#         quality = 'Delicious!'
#     # quality = predict(feature1, feature2, feature3) # this will just be good/bad/declious?
#     st.success(f'The predicted wine quality is {quality}') # or we predict your wine to be [...]?