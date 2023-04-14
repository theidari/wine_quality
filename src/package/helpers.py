# --------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------ All libraries, variables and functions are defined in this file ---------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# main dependencies and setup
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport # data statistic profiling
from pathlib import Path

# ml dependencies and setup
from sklearn.cluster import KMeans # KMeans
from sklearn.decomposition import PCA # PCA
from sklearn.preprocessing import StandardScaler # StandardScale to resize the distribution of values 
from sklearn.metrics import silhouette_score # Silhouette method
from sklearn.metrics import calinski_harabasz_score # Calinski Harabasz method

from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report

# Import sampling 
from sklearn.model_selection import train_test_split # Import the train_test_learn module
from imblearn.over_sampling import RandomOverSampler # Import the RandomOverSampler module form imbalanced-learn

# Import models:
from sklearn.linear_model import LogisticRegression # Logistic Regression
from sklearn.ensemble import RandomForestClassifier # RandomForest
import xgboost as xgb # Extreme gradient boosting (XGBoost)
import lightgbm as lgb # LightGBM


from sklearn.base import BaseEstimator, TransformerMixin # estimators and transformers 

import statsmodels.api as sm

# plotting dependencies and setup  
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

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
    print(f"Number of Rows\ntrain: {train_df.shape[0]}\ntest: {test_df.shape[0]}")
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
        query_train = f"""train_{df}.to_csv('../data/splitdata/train_{df}.csv', index=False)"""
        exec(query_train)
        query_test = f"""test_{df}.to_csv('../data/splitdata/test_{df}.csv', index=False)"""
        exec(query_test)
        # show report
        profile_report = ProfileReport(locals()[f"train_{df}"], explorative=True, dark_mode=True)
        profile_report_file_path = Path(f'../results/{df}_profile.html')
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

print(f"☑ helpers is imporetd")    
# --------------------------------------------------------------------------------------------------------------------------------------------