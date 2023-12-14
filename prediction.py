import joblib
import numpy as np

def predict_yield(input_values, model):
    """
    Predict the class of a given data point.
    """
    return model.predict(input_values)