import streamlit as st
import sklearn
import pickle as pk
import pandas as pd

#load model
with open('model.pickle', 'rb') as filename:
    model = pk.load(filename)
st.title('Salary Prediction System')
st.image('https://media.licdn.com/dms/image/v2/D4E12AQHL_sTE91rFVg/article-cover_image-shrink_720_1280/B4EZc7u8urG4AI-/0/1749053853357?e=2147483647&v=beta&t=KfrApL1NwynAXVZa7ZqpUfqbOr7qJZLe7XVau7zQQqg')

# taking input from user
st.header('Enter all values for salary prediction')
job = st.text_input("Enter the Job Title")
gender = st.radio("Enter Gender", ["Female","Male"])
age = st.number_input("Age = ", 20, 70)
exp = st.number_input("Experience = ", 0, 30)
edu = st.selectbox("Pick the Education Level", ["Bachelor's", "Master's","PhD"])
if edu == "Bachelor's":
    b = 1;m = 0;p = 0
elif edu == "Master's":
    b = 0; m =1; p = 0
else:
    b = 0; m = 0; p =1

df = pd.DataFrame(
    [[age,exp,b,m,p]],columns=['Age',"Years of Experience","Bachelor's","Master's","PhD"])

# for prediction
if st.button("Predict"):
    st.success("The data is submitted")
    st.balloons()
    st.write(df)
    result = model.predict(df)
    st.write("The Salary is Rs. ",int(result[0]))