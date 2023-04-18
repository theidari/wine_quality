<p align="center">
  <img src="https://github.com/theidari/wine_quality/blob/main/asset/header.png" width=400px>
    </p>
<h3>Introduction</h3>
<p align="justify">The goal of this machine learning project is to predict the quality of a wine from features describing its physical chemistry. While wineries conduct both chemical analysis and wine tastings to analyze their wine, the impact of the entire chemistry on taste is not commonly measured. With machine learning the goal is to bridge this gap, and highlight patterns and relationships that may not be apparent. This could be use or support wineries in their quality assurance or wine tasting, hopefully bringing some helpful new insight to lead to better tasting wine.</p>
<h4>Methods, Software and Attribution</h4>
The analyses were performed using 

Following programming languages, software, and libraries were used in this project:

```
├── assets
│   ├── header.png                                <- project header image used in the README.
│
├── data
│   ├── splitdata 
|       ├── test_df_red.csv                  
|       ├── test_df_white.csv                   
|       ├── train_df_red.csv                   
|       ├── train_df_white.csv                   
│   ├── normalizedata                        
│       ├── test.csv                                 
│       ├── train.csv                                
│
├── result
│   ├── test_df_red_profile.html                 
│
├── src                                    
│
├── LICENSE                                       <- license file.
│
├── README.md                                     <- this readme file.
|
├── requirements.txt                              <- list of all the dependencies with their versions(used for Streamlit).
```

<h3>Wine Quality Predictor</h3>
<p align="justify">A tool designed to predict wine quality, based on a set of input features. The predictor employs statistical models or machine learning algorithms to learn from a dataset of labeled examples and to make predictions for new, unseen samples. The features used can vary depending on the type of wine and the available data, but may include attributes such as acidity, pH, alcohol content, sugar content, or sensory descriptors. The accuracy and reliability of the predictor depend on the quality and representativeness of the dataset, the choice of modeling method, and the validation procedures used to evaluate its performance. Wine quality predictors can be useful for wine makers, sellers, and consumers, as they can provide valuable information about the expected taste, aroma, and overall appeal of a wine, and help to optimize production or selection decision</p>
<h3>Conclusion</h3>
<h3>references</h3>
<ol>
<li>Collection of wines from Vinho Verde region <a href="https://archive.ics.uci.edu/ml/datasets/wine+quality"><b>⍈</b></a></li>
<li>P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. mModeling wine preferences by data mining from physicochemical properties.
In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236. <a href="https://www.sciencedirect.com/science/article/pii/S0167923609001377?via%3Dihub"><b>⍈</b></a></li>
</ol>
<h4>Contribution</h4>
<p align="justify">We welcome pull requests! However, if you are planning to make significant changes, please initiate a discussion by opening an issue to share your ideas and contributions.</p>
