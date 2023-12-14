import streamlit as st
import joblib
import sklearn
import pandas
import numpy as np
from prediction import predict_yield

model = joblib.load(r'Model/Linear_Regression_Optimum_Model.joblib')

st.set_page_config(page_title="Blueberry Yield Prediction",layout="wide")

features = ['clonesize', 'honeybee', 'bumbles', 'andrena', 'osmia','AverageOfUpperTRange','AverageOfLowerTRange','AverageRainingDays']

st.markdown("<h1 style='text-align: center;'>Blueberry Yield Prediction Application</h1>", unsafe_allow_html=True)

def main():
    with st.form('prediction_form'):

        st.header('Enter the input for following features:')

        clonesize = st.number_input('The average blueberry clone size in the field (in m2)')
        honeybee = st.number_input('Honeybee density in the field in (in bees/m2/min)')
        bumbles = st.number_input('Bumblebee density in the field (in bees/m2/min)')
        andrena = st.number_input('Andrena bee density in the field (in bees/m2/min)')
        osmia = st.number_input('Osmia bee density in the field (in bees/m2/min)')
        AverageOfUpperTRange = st.number_input('The average of the upper band daily air temperature (in ℃)')
        AverageOfLowerTRange = st.number_input('The average of the lower band daily air temperature (in ℃)')
        AverageRainingDays = st.number_input('The average of raining days of the entire bloom season (in Days)')

        submit = st.form_submit_button("Predict Yield")

    if submit:

        input_values = np.array([clonesize, honeybee, bumbles, andrena, osmia, AverageOfUpperTRange, AverageOfLowerTRange, AverageRainingDays]).reshape(1,-1)

        pred = predict_yield(input_values, model)

        st.success('The forecasted yield is {}'.format(round(pred[0],2)))

if __name__ == '__main__':

    main()

