import requests
from datetime import timedelta, datetime

import pandas as pd

from prefect import task, Flow
from prefect.schedules import IntervalSchedule

@task(max_retries=3, retry_delay=timedelta(5))
def predict(input_data_path:str):
    """
    This task load the saved model, input data and returns prediction.
    If failed this task will retry 3 times at 5 min interval and fail permenantly.
    """
    
    classifier = joblib.load('classifier.pkl')
  
    df = pd.read_csv(input_data_path)
  
    prediction = classifier.predict(df)
  
    return jsonify({'prediction': list(prediction)})
  
  
@task(max_retries=3, retry_delay=timedelta(5))
def save_prediction(data, output_data_path:str):
    """
    This task will save the prediction to an output file. 
    If failed, this task will retry for 3 times and fail permenantly.
    """
    with open(output_data_path, 'w') as f:
      f.write(data)
    

# Create a schedule object. 
# This object starts 5 seconds from the time of script execution and repeat once a week. 
schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=5),
    interval=timedelta(weeks=1),
)

# Attach the schedule object and orchastrate the workflow.
with Flow("predictions", schedule=schedule) as flow:
    prediction = predict("./input_data.csv")
    save_prediction(prediction "./output_data.csv")
    