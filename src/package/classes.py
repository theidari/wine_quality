# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------- All classes are defined in this file ---------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# package dependencies and setup
from package.helpers import *  # libraries, variables and functions

# --------------------------------------------------------------------------------------------------------------------------------------------
# pipline classes
# handle skewness by cube root _______________________________________________________________________________________________________________
class CubeRootTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, df, columns_skewness=None):
        self.df = df
        if columns_skewness is None:
            result_df = skewness_report(df)
            critical_skewness = result_df.loc[(result_df['category'] == 'Moderate Skewness') |
                                              (result_df['category'] == 'High Skewness'), 'c_name']
            self.columns_skewness = critical_skewness
        else:
            self.columns_skewness = columns_skewness
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        if not set(self.columns_skewness).issubset(X.columns):
            print("One or more features are not in the dataframe")
            return X
        
        X = X.copy()
        X[self.columns_skewness] = np.cbrt(X[self.columns_skewness])
        return X

print(f"☑ classes is imporetd")     
# --------------------------------------------------------------------------------------------------------------------------------------------
