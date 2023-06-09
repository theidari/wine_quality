# --------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------ All libraries, variables and functions are defined in this file ---------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# main dependencies and setup
import os
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport # data statistic profiling
from pathlib import Path
import datetime as datetime
import statsmodels.api as sm

# ml dependencies and setup
from sklearn.pipeline import Pipeline # pipeline
from sklearn.cluster import KMeans # KMeans
from sklearn.decomposition import PCA # PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler # StandardScale to resize the distribution of values 
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report, roc_curve, auc, r2_score, mean_squared_error, accuracy_score
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.base import BaseEstimator, TransformerMixin # estimators and transformers 

from mord import LogisticAT

# Import sampling 
from sklearn.model_selection import train_test_split, learning_curve # Import the train_test_learn module
from imblearn.over_sampling import RandomOverSampler # Import the RandomOverSampler module form imbalanced-learn

# Import models:
from sklearn.linear_model import LogisticRegression, LinearRegression # Logistic Regression
from sklearn.ensemble import RandomForestClassifier # RandomForest
import xgboost as xgb # Extreme gradient boosting (XGBoost)
import lightgbm as lgb # LightGBM

import tensorflow as tf
import keras_tuner as kt

# streamlit dependencies and setup
import pickle

# plotting dependencies and setup  
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import matplotlib.pyplot as plt
# package dependencies and setup
from package.constants import * # constants

# --------------------------------------------------------------------------------------------------------------------------------------------
# functions
# investigation functions ____________________________________________________________________________________________________________________
def data_splitter(df, test_size):
    """
    Splits a DataFrame into training and testing subsets using scikit-learn's `train_test_split` function,
    and returns the two subsets.

    Args:
        df: A pandas DataFrame to split.
        test_size: The proportion of the dataset to include in the test split.

    Returns:
        A tuple containing two pandas DataFrames: the training subset and the testing subset.
    """
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=42)
    train_df.reset_index(drop=True, inplace=True)
    test_df.reset_index(drop=True, inplace=True)
    print(f"Number of Rows in\ntrain: {train_df.shape[0]}\ntest: {test_df.shape[0]}")
    return train_df, test_df


def convert_and_profile(dfs):
    """
    For each DataFrame in a list, saves its train and test subsets as CSV files,
    and generates and saves a profile report for the train subset.

    Args:
        dfs: A list of DataFrames.

    Returns:
        None.
    """
    for i, df in enumerate(dfs):
        # save train and test 
        df_query= f"""{df}.to_csv('{DATA_URL}{df}.csv',index=False)"""
        exec(df_query)
        # show report
        query_profile_report = f"""ProfileReport({df}, explorative=True, dark_mode=True)"""
        profile_report = eval(query_profile_report)
        profile_report_file_path = Path(f"{OUTPUT_URL}{df}_profile.html")
        try:
            profile_report_file_path.resolve(strict=True)
        except FileNotFoundError:
            profile_report.to_file(profile_report_file_path)

                    
def skewness_report(df):
    """
    Computes the skewness of each numerical column in a pandas DataFrame,
    and categorizes them as light, moderately, or heavily skewed.

    Args:
        dfs: A pandas DataFrames that will be analyzed.
        
    Returns:
        A new DataFrame with three columns: 'c_name' as a column name, 'skewness', and 'category'.
    """
    df_features = df.iloc[:, :-1]
    skew_values = list(df_features.skew())
    skew_categories = []
    for value in skew_values:
        if abs(value) <= 0.5:
            skew_categories.append("Low Skewness")
        elif abs(value) <= 1:
            skew_categories.append("Moderate Skewness")
        else:
            skew_categories.append("High Skewness")
    result_df = pd.DataFrame({'c_name': df_features.columns, 'skewness': skew_values, 'category': skew_categories})
    return result_df


# plotting function __________________________________________________________________________________________________________________________ 
def violin_plot(df):
    """
    Create a violin plot for a DataFrame

    Args:
        df: A pandas DataFrames that will be analyzed.
        
    Returns:
        A plot includes a statistical summary of the features.
    """
    # ceate subplots with one row and number of columns equal to the number of columns in the df
    fig = make_subplots(rows=1, cols=len(df.columns), horizontal_spacing=0.02)
    
    # define a color gradient for the violins based on color data in (./src/package/)
    colors = np.linspace(COLORSET[0], COLORSET[1], len(df.columns)).tolist()
    
    # iterate through each column in the df and add a violin trace to the plot
    for i, column in enumerate(df.columns):
        
        # define the color for the violin based on the color gradient
        rgb_tuple = tuple(colors[i])
        rgb_string = 'rgb({}, {}, {})'.format(*rgb_tuple)
        
        # if the column name contains more than two words, split the name into two lines for better readability
        if len(column.split()) >= 3:
            first_line = column.split()[0].upper()
            second_line = column.split()[1].upper()+" "+column.split()[2].upper()
            name = f"{first_line}<br>{second_line}"
        else:
            name = column.upper()
            
        # add a violin trace to the plot
        fig.add_trace(
            go.Violin(
                y=df[column],
                name=name,
                box_visible=True,
                meanline_visible=True,
                fillcolor=rgb_string,
                opacity=0.7,
                line=dict(color='black', width=1),
                marker=dict(color='black', size=5, opacity=0.3),
                showlegend=False
            ),
            row=1,
            col=i+1
        )
    
    # update the layout of the plot
    fig.update_layout(
        height=700,
        width=1500, 
        xaxis=dict(color= 'black',
                   showline=True,
                   linewidth=1,
                   linecolor='black'), 
        yaxis=dict(title=dict(text='Counts', font=dict(size= 14, color= 'black', family= "calibri"))),
        plot_bgcolor='#f7f7f7',
        paper_bgcolor="#ffffff"
    )
    
    # update the x and y axes for each column
    for i, column in enumerate(df.columns):
        fig.update_xaxes(tickcolor='#ffffff',
                tickfont=dict(size= 14, family='calibri', color='black' ),
                                         showline=True, linewidth=3, linecolor='#f7f7f7', mirror=True)
        fig.update_yaxes(tickangle=-90, tickfont=dict(size= 14, family='calibri', color='black'), 
                                                      showline=True, linewidth=3, linecolor='#f7f7f7', mirror=True)

    return fig.show() # show the plot


# modeling functions _________________________________________________________________________________________________________________________


print(f"☑ helpers have been imported")    
# --------------------------------------------------------------------------------------------------------------------------------------------
