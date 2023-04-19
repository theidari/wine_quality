import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

# Load model file for white
model_white = pickle.load(open('Resources/svm_model_white.pkl', 'rb'))
# Load model file for red
model_red = pickle.load(open('Resources/svm_model_red.pkl', 'rb'))


# Streamlit elements 
st.title('Wine Quality Prediction')
st.write('Trained with wine data from Vinho Verde - Portugal')
st.header('Enter wine chemistry below')

tab1, tab2 = st.tabs(['White Wine', 'Red Wine'])

with tab1:
    # User feature input
    feature1 = st.number_input('Fixed Acidity', min_value = 1.5, max_value = 2.5, value=2.0, key = 'white FA')
    feature2 = st.number_input('Volatile Acidity', min_value = 0.35, max_value = 1.15, value=0.5, key = 'white VA')
    feature5 = st.number_input('Chlorides', min_value = 0.2, max_value = 0.53, value=0.3, key = 'white C')
    feature6 = st.number_input('Free Sulfur Dioxide', min_value = 1.44, max_value = 4.8, value=2.5, key = 'white FSD')
    feature9 = st.number_input('pH Level', min_value = 2.72, max_value = 3.9, value=3.2, key = 'white pH')
    feature10 = st.number_input('Sulphates Content', min_value = 0.6, max_value = 1.07, value=0.8, key = 'white SC')
    feature11 = st.number_input('Alcohol Content', min_value = 8.0, max_value = 14.9, value=10.0, key = 'white AC')

    if st.button('Predict Quality', key = 'white button'):

        # Collect user input
        user_input = [feature1, feature2, feature5, feature6, feature9, feature10, feature11]
        
        model = model_white 
        
        input = pd.DataFrame([user_input],\
                         columns=['fixed acidity','volatile acidity','chlorides','free sulfur dioxide', \
                                   'pH', 'sulphates', 'alcohol']) 
        
    
        quality = model.predict(input)
        
        if quality == 0:
            quality = 'Bad'
        if quality == 1:
            quality = 'Delicious!'

        st.success(f'The predicted wine quality is {quality}')

with tab2: 
    # User feature input
    feature2 = st.number_input('Volatile Acidity', min_value = 0.35, max_value = 1.15, value=0.5, key = 'red VA')
    feature3 = st.number_input('Citric Acid', min_value = 0.0, max_value = 0.95, value=0.0, key = 'red CA')
    feature4 = st.number_input('Residual Sugar', min_value = 0.8, max_value = 3.0, value=1.0, key = 'red RS')
    feature5 = st.number_input('Chlorides', min_value = 0.2, max_value = 0.53, value=0.3, key = 'red C')
    feature9 = st.number_input('pH Level', min_value = 2.72, max_value = 3.9, value=3.2, key = 'red pH')
    feature10 = st.number_input('Sulphates Content', min_value = 0.6, max_value = 1.07, value=0.8, key = 'red SC')
    feature11 = st.number_input('Alcohol Content', min_value = 8.0, max_value = 14.9, value=10.0, key = 'red AC')

    if st.button('Predict Quality', key = 'red button'):

        # Collect user input
        user_input = [feature2, feature3, feature4, feature5, feature9, feature10, feature11]

        model = model_red

        input = pd.DataFrame([user_input],\
                         columns=['volatile acidity','citric acid', 'residual sugar','chlorides', \
                                   'pH', 'sulphates', 'alcohol'])
        
        quality = model.predict(input)
        if quality == 0:
            quality = 'Bad'
        if quality == 1:
            quality = 'Delicious!'
        
        st.success(f'The predicted wine quality is {quality}') 