import pandas as pd
from joblib import load
import os


def predict_stroke(predict_list):
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../"))
    pipeline = load(f"{dir_path}/stroke_model.joblib")
    result = pipeline.predict(pd.DataFrame(predict_list, index=[0]))
    
    if int(result[0]) == 1:
        prediction_result = "Please consult a doctor. Based on your inputs you are likely to get stroke."
    else:
        prediction_result = "Congratulations! Based on your inputs you are not likely to get a stroke."

    return prediction_result

