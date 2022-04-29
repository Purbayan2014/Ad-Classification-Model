import streamlit as st
import numpy as np
import pandas as pd

import requests



API_KEY = "iYwv7fdzQtEg5OT77SDtB3TjPFTIBShtT4C7yX-08UcF"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


st.title('Advertisement Success Prediction')


# setting up the form

daily_time = st.number_input('Enter Your Daily Time')

age = st.number_input('Enter Your Age')

areaincome = st.number_input('Enter Your Area Income')

dailyinternetuse = st.number_input('Enter Your Daily Internet Use')

adtopicline = st.text_input('Enter Advertisement Topic Line')

city = st.text_input('Enter City')

gender = st.selectbox('Enter Gender', ['Male', 'Female'])

country = st.text_input('Enter Country Name')

timestamp = st.text_input('Enter Timestamp')




try:
    if st.button('Predict'):

        input_features = [[daily_time, age, areaincome, dailyinternetuse,
                           adtopicline, city, gender, country, timestamp]]

        payload_scoring = {"input_data": [{"fields": [
            ["daily_time", "age", "areaincome", "dailyinternetuse", "adtopicline", "city", "gender", "country", "timestamp"]],
            "values": input_features}]}

        response_scoring = requests.post('https://jp-tok.ml.cloud.ibm.com/ml/v4/deployments/043b20c7-ee91-4c49-bcaf'
                                         '-493e51da04a9/predictions?version=2022-03-08', json=payload_scoring,
                                         headers={'Authorization': 'Bearer ' + mltoken})

        print("Scoring response")
        print(response_scoring.json())

        ans = response_scoring.json()['predictions'][0]['values']

        finalprob = ans[0][1][0]

        if finalprob > 50:
            st.markdown(
                "Based on the above factors,the user Viewed the Advertisement")

        else:
            st.markdown(
                "Based on the above factors,the user did not View the Advertisement")


except:
    st.markdown("Hang on,might be some mistake in the input,do check it again")
