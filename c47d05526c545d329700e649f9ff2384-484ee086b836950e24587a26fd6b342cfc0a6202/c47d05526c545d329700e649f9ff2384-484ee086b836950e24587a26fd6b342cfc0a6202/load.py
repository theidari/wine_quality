import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('titanic.csv')

x = df[df.columns.difference(['Survived'])
y = df['Survived']
       
classifier = RandomForestClassifier()
classifier.fit(x, y)