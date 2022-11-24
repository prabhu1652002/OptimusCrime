# Importing pakages
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# c.execute("CREATE DATABASE ebike")


def main():
    st.title("Crime Rate Prediction and Analysis")
    st.subheader("Vijit Kumar PES1UG20CS500")    
    st.subheader("Rhea Sudheer PES1UG20CS580")    
    st.subheader("Basavaprabhu PES1UG20CS631")    

    df = pd.read_csv("final.csv")
    for index,row in df.iterrows():
        row['STATE/UT']=row['STATE/UT'].upper()
        

    states=df["STATE/UT"]
    states_set=set()
    for state in states:
        s=state.upper()
        states_set.add(s)
    districts=dict()
    for i in states:
        districts[i]=set()
    for index, row in df.iterrows():
        districts[row["STATE/UT"]].add(row["DISTRICT"])
    for i in districts.keys():
        set(districts[i])

    for i in districts.keys():
        districts[i]=sorted(districts[i])


    states_set=sorted(states_set)
    choosen_state=st.selectbox("Choose state:",states_set)
    choosen_district=st.selectbox("Choose district:",districts[choosen_state])
    choosen_state=choosen_state.lower()
    choosen_district=choosen_district.lower()

    if st.button("Predict"):
        display(choosen_state,choosen_district)


def display(choosen_state,choosen_district):
    encoded_state=0
    encoded_district=0
    df_enc=pd.read_csv('encoding.csv')
    for index, row in df_enc.iterrows():
        if([choosen_state,choosen_district]==[row["STATE/UT"],row["DISTRICT"]]):
            encoded_state=row["State_code"]
            encoded_district=row["District_code"]
            # break
    # st.write(encoded_state)
    # st.write(encoded_district)
    df_rape=pd.read_csv("rape_pred.csv")
    df_kidabd=pd.read_csv("kidabd_pred.csv")
    df_dowry=pd.read_csv("dowry_pred.csv")
    df_assault=pd.read_csv("assault_pred.csv")
    df_insult=pd.read_csv("insult_pred.csv")

    for index, row in df_rape.iterrows():
        val=int(row["Prediction"].round())
        avg=df_rape["Prediction"].mean()
        if row["STATE/UT"]==encoded_state and row["DISTRICT"]==encoded_district:
            if val>=avg:
                st.warning(f"High rate of Rape Cases in this state", icon="⚠️")
            else:
                st.success(f"Rape crimes are less frequent here")

    for index, row in df_kidabd.iterrows():
        val=int(row["Prediction"].round())
        avg=df_kidabd["Prediction"].mean()
        if row["STATE/UT"]==encoded_state and row["DISTRICT"]==encoded_district:
            if val>=avg:
                st.warning(f"High rate of Kidnapping and abduction Cases in this state", icon="⚠️")
            else:
                st.success(f"Kidnapping and abduction are less frequent here")
    for index, row in df_dowry.iterrows():
        val=int(row["Prediction"].round())
        avg=df_dowry["Prediction"].mean()
        if row["STATE/UT"]==encoded_state and row["DISTRICT"]==encoded_district:
            if val>=avg:
                st.warning(f"High rate of Dowry Death Cases in this state", icon="⚠️")
            else:
                st.success(f"Dowry Deaths are less frequent here")
    for index, row in df_assault.iterrows():
        val=int(row["Prediction"].round())
        avg=df_assault["Prediction"].mean()
    
        if row["STATE/UT"]==encoded_state and row["DISTRICT"]==encoded_district:
            if val>=avg:
                st.warning(f"High rate of Assault on women Cases in this state", icon="⚠️")
            else:
                st.success(f"Assault on women are less frequent here")
    for index, row in df_insult.iterrows():
        val=int(row["Prediction"].round())
        avg=df_insult["Prediction"].mean()
    
        if row["STATE/UT"]==encoded_state and row["DISTRICT"]==encoded_district:
            if val>=avg:
                st.warning(f"High rate of Insult to modesty of women Cases in this state", icon="⚠️")
            else:
                st.success(f"Insult to modesty of women are less frequent here")







if __name__ == '__main__':
    main()
