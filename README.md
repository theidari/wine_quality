<p align="center">
  <img src="https://github.com/theidari/wine_quality/blob/main/asset/header.png" width=400px>
</p>
<p align="center"><a href="https://theidari-wine-quality-appstreamlit-benjamin-1l3eqb.streamlit.app/#wine-quality-prediction"><img src="https://shields.io/badge/streamlit-Wine%20Quality%20Predictor-red?logo=streamlit&style=flat-square"></a></p>
<h3><img src="https://shields.io/badge/▁-red?&style=flat" height=15px> Introduction</h3>
<p align="justify">
&emsp;&emsp;Wine is an alcoholic beverage that is traditionally made by fermenting grapes, though it can also be made from other fruits like apples and berries. To make wine, grapes are harvested, crushed to extract the juice, and then fermented with yeast to convert the natural sugars into alcohol. The resulting wine can range from sweet to dry and is enjoyed in a variety of settings, from casual gatherings to formal events. Wine is culturally and historically significant and has been an integral part of human civilization for thousands of years. Today, wine is produced in various regions worldwide, each with its unique styles, flavors, and characteristics.<a href="https://github.com/theidari/wine_quality#references"><b>[1]</b></a><br>
&emsp;&emsp;Portugal is among the top ten wine-exporting countries, with a $1.1 billion (2.7%) market share in 2022 <a href="https://github.com/theidari/wine_quality#references"><b>[2]</b></a>,
and its vinho verde wine, primarily from the northwest region, has seen a 36% increase in exports from 1997 to 2007. To support the wine industry's growth, new technologies are being invested in for both wine making and selling processes. Certification and quality assessment are crucial to preventing illegal adulteration and ensuring the production of high-quality wine. Quality evaluation is typically conducted as part of the certification process, helping to identify critical factors involved in wine production and classify wines according to their quality levels, such as premium brands. This information is also used to determine pricing.<a href="https://github.com/theidari/wine_quality#references"><b>[4]</b></a><br>
&emsp;&emsp;Wine quality evaluation involves both physicochemical and sensory tests. Physicochemical laboratory tests, such as density, alcohol content, and pH measurements, are commonly used to characterize wine. Meanwhile, sensory tests rely on trained individuals to assess the taste, aroma, and overall quality of the wine. In this machine learning project, the <ins><b>goal</b></ins> is to predict the quality of a wine based on features describing its physical chemistry. While wineries conduct chemical analyses and wine tastings to analyze their wine, the impact of the entire chemistry on taste is not commonly measured. Machine learning aims (<ins><b>motivation</b></ins>) to bridge this gap and identify patterns and relationships that may not be immediately apparent. This approach (<ins><b>use cases</b></ins>) can support wineries in their quality assurance or wine tasting, hopefully leading to better-tasting wine.
</p>

<h3><img src="https://shields.io/badge/▁-red?&style=flat" height=15px> Data</h3>
<p align="justify">
&emsp;&emsp;The datasets used in this research are available at <a href="http://www3.dsi.uminho.pt/pcortez/wine/">Wine Quality Datasets</a> and relate to the red and white variants of the Portuguese "Vinho Verde" wine <a href="https://www.vinhoverde.pt/en/homepage">ℹ</a>, with 1599 and 4898 instances, respectively. Due to privacy and logistic issues, the datasets only contain physicochemical (11 input attributes) and sensory (output) variables. The output attribute represents the median of at least three evaluations made by wine experts who rated the wine quality on a scale from 0 (very bad) to 10 (very excellent). The datasets do not include information about grape types, wine brands, or selling prices.<br>
&emsp;&emsp;The datasets were created in 2009 by Paulo Cortez, Antonio Cerdeira, Fernando Almeida, Telmo Matos, and Jose Reis. They were used in a study titled "Modeling wine preferences by data mining from physicochemical properties" by the same authors, published in the Decision Support Systems journal.
</p>
<h4>Input attributes (based on physicochemical tests):</h4>
<ol align="justify">
<li><b>Fixed Acidity:</b> set of low volatility organic acids such as malic, lactic, tartaric or citric acids. <a href="https://sinatech.info/en/acetic-volatile-acidity-in-wine-cider-vinegars-and-juices/#:~:text=Fixed%20acidity%20corresponds%20to%20the,of%20a%20distillation%20process%3A%20formic">ℹ</a></li>
<li><b>Volatile Acidity:</b> a measure of the wine's volatile (or gaseous) acids. <a href="https://extension.psu.edu/volatile-acidity-in-wine#:~:text=What%20Is%20Volatile%20Acidity%3F,smell%20and%20taste%20of%20vinegar.">ℹ</a></li>
<li><b>Citric Acid:</b> to increase acidity, complement a specific flavor or prevent ferric hazes. <a href="https://wineserver.ucdavis.edu/industry-info/enology/methods-and-techniques/common-chemical-reagents/citric-acid#:~:text=Citric%20acid%20is%20often%20added,acid%20is%20its%20microbial%20instability.">ℹ</a></li>
<li><b>Residual Sugar:</b> is from the natural grape sugars left in a wine after the alcoholic fermentation finishes. <a href="https://whicherridge.com.au/blog/what-is-residual-sugar-in-wine/#:~:text=Sweetness%20in%20wine%20is%20called,the%20sweeter%20the%20wine%20is.">ℹ</a></li>
<li><b>Chlorides:</b> is the amount of salt in the wine. <a href="https://www.scielo.br/j/cta/a/HQsrPrPMNZYgRzSKtrjHyHh/?format=pdf&lang=en
">ℹ</a></li>
<li><b>Free Sulfur Dioxide:</b> it prevents microbial growth and the oxidation of wine. <a href="https://www.oiv.int/public/medias/7840/oiv-collective-expertise-document-so2-and-wine-a-review.pdf">ℹ</a></li>
<li><b>Total Sulfur Dioxide:</b> is the amount of free + bound forms of SO2. <a href="https://www.oiv.int/public/medias/7840/oiv-collective-expertise-document-so2-and-wine-a-review.pdf">ℹ</a></li>
<li><b>Density:</b> sweeter wines have a higher density. <a href="https://www.aqua-calc.com/page/density-table/substance/alcoholic-blank-beverage-coma-and-blank-wine-coma-and-blank-table-coma-and-blank-red-coma-and-blank-merlot">ℹ</a></li>
<li><b>pH:</b> Typically, the pH level of a wine ranges from 3 to 4. <a href="https://www.winemag.com/2019/06/19/what-is-acidity-in-wine/">ℹ</a></li>
<li><b>Sulphates:</b> are naturally occurring and an added preservative found in wine and many other foods and beverages. <a href="https://www.winedeals.com/blog/post/sulfites-in-wine-what-they-are-and-how-they-affect-you#:~:text=What%20Are%20Sulfites%20and%20Why,of%20yeast%20metabolism%20during%20fermentation.">ℹ</a></li>
<li><b>Alcohol:</b> the amount of alcohol in wine. <a href="https://winefolly.com/tips/the-lightest-to-the-strongest-wine/">ℹ</a></li>
</ol>

<h3><img src="https://shields.io/badge/▁-red?&style=flat" height=15px> Project Overview</h3>
<ul>
<li><b>step 1 - Data preprocessing:</b> Normalization, oversampling, and scaling</li> 
<li><b>step 2 - Compare performance of multiple models:</b> Decision Tree, Logistic Regression, Support Vector</li> 
<li><b>step 3 - Optimization:</b> Learning curves, feature selection</li> 
<li><b>step 4 - Demonstration:</b> Simple app using Streamlit</li> 
</ul>



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
<h3>Model Analysis</h3>
<p align="justify">Despite less data point, logistic regression model performs slightly higher with red wine dataset than the white one regarding model accuracy (80% vs 78%). Both model predict low quality wine in comparison to high quality wine (higher f1-score). However, there is a concern in significant difference between precision and recall in both red & white dataset. In specific, with red wine dataset, precision is considerably higher in low-quality category but the recall rate is greatly lower. Similarly, with white wine dataset, the model poorly predicts high-quality category by approximately 20% in terms of precision and recall rate. This may signal a likeliness of model unfitting.
Red Wine
The wide gap between training and validation accuracy indicates that the logistic regression model is highly bias and does not capture enough complexity for adequate prediction. Moreover, two lines crossing each other at nearly the end of the graphs means that the model generally require more data point and time to train. This can require more time consumption for data collection and merging.
White Wine
It’s worth to notice that the training accuracy reduce over time when adding more data points, meaning the model is underfit and may require more optimization activity.
</p>

<h3>Model Optimization</h3>
<p align="justify">The machine learning algorithm that ended up performing the best was the support vector machine. To optimize the model, we first utilize feature importance. I decided to drop the bottom 4 features for both red and white wine to boost accuracy, but we were only able to achieve higher accuracy for white wine (from 64% to 79%). Red wine accuracy on the other had decreased somewhat, but is still very accurate. It may be more sensitive to dropping columns due to the dataset size compared to white wine. After optimization, we used a cross validation score learning curve to see if the model isn’t overfitting or underfitting the data. Since we see both the training and validation scores converge in the middle as the number of training examples increases, it indicates that the model is fitting and generalizing well to new data. Now that we know our model is fitting well, it’s time to evaluate the accuracy and performance. The red wine model has an excellent area under curve value of 96, which means it has a 96% chance to be able to distinguish between positive and negative classification. The white wine model performs at an area under curve of 83%. This indicates that both models are performing well.</p>
<h3>Conclusion</h3>
<p align="justify">After testing various models, SVM was the final model selected based on highest accuracy between models. The model for red wine performed at 98% and 69% precision on testing data for bad and delicious wines respectively, where the white wine had 83% and 70% for bad and delicious wines. Both red and white models differed in feature importance as expected, validating our choice to run separate models for each. Further work could be done with this model to refine the accuracy on wine quality in general, but also into more distinct outputs. For example, move to three to four outputs of quality to achieve more informative results.</p>
<h3>references</h3>
<ol>
<li>Wikimedia Foundation. (2023, April 12). Wine. Wikipedia. Retrieved April 19, 2023.<a href="https://en.wikipedia.org/wiki/Wine"><b>➲</b></a></li> 
<li>Workman, D. (n.d.). Wine Exports by Country. worlds top exports. Retrieved April 18, 2023. <a href="https://www.worldstopexports.com/wine-exports-country/"><b>➲</b></a></li>
<li>Collection of wines from Vinho Verde region <a href="https://archive.ics.uci.edu/ml/datasets/wine+quality"><b>➲</b></a></li>
<li>P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. mModeling wine preferences by data mining from physicochemical properties.
In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236. <a href="https://www.sciencedirect.com/science/article/pii/S0167923609001377?via%3Dihub"><b>➲</b></a></li>
</ol>
<h4>Contribution</h4>
<p align="justify">We welcome pull requests! However, if you are planning to make significant changes, please initiate a discussion by opening an issue to share your ideas and contributions.</p>
