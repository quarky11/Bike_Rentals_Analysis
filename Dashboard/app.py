import pandas as pd
import streamlit as st
from PIL import Image
import datetime
import plotly.express as px
import plotly.graph_objects as go

#import data
df_hour = pd.read_csv("Dashboard/hour.csv")

#cleaning outlier
Q1 = (df_hour['cnt']).quantile(0.25)
Q3 = (df_hour['cnt']).quantile(0.75)
IQR = Q3 - Q1

maximum = Q3 + (1.5*IQR)
minimum = Q1 - (1.5*IQR)

kondisi_lower_than = df_hour['cnt'] < minimum
kondisi_more_than = df_hour['cnt'] > maximum
df_hour.drop(df_hour[kondisi_lower_than].index, inplace=True)
df_hour.drop(df_hour[kondisi_more_than].index, inplace=True)

#cleaning data1
weather_mapping = {
    1: "Clear, Few clouds",
    2: "Mist + Cloudy, Mist",
    3: "Light Snow, Light Rain clouds",
    4: "Heavy Rain"
}
df_hour['weather_desc'] = df_hour['weathersit'].map(weather_mapping)

season_mapping = {
    1: "spring",
    2: "summer",
    3: "fall",
    4: "winter"
}
df_hour['season_desc'] = df_hour['season'].map(season_mapping)

Holiday_mapping = {
    0: "Working hour",
    1: "Holiday"
}

df_hour['day_desc'] = df_hour['holiday'].map(Holiday_mapping)

#Cleaning data2 (Binning Technique)

cutoff = [-1,3,9,15,20,23]
labels = ["Dini Hari","Pagi Hari","Siang Hari","Sore Hari","Malam Hari"]
df_hour ['Time_Desc'] = pd.cut(df_hour["hr"],bins=cutoff,labels=labels)

#EDA

df_rentals_byseason = df_hour.groupby(by="season_desc", as_index=False
).agg(
    sum_hour=("instant", "nunique"),   # Jumlah hari unik
    total_rentals=("cnt", "sum"),     # Total rental sepeda
    rentals_per_hours =("cnt", "mean")      # Rata-rata rental sepeda
).sort_values(by="total_rentals", ascending=False)

df_rentals_byweather= df_hour.groupby(by="weather_desc", as_index=False
).agg(
    sum_hour=("instant", "nunique"),   # Jumlah hari unik
    total_rentals=("cnt", "sum"),     # Total rental sepeda
    rentals_per_hours =("cnt", "mean")      # Rata-rata rental sepeda
).sort_values(by="total_rentals", ascending=False)

df_rentals_bytimedesc= df_hour.groupby(by="Time_Desc", as_index=False
).agg(
    sum_hour=("instant", "nunique"),   # Jumlah hari unik
    total_rentals=("cnt", "sum"),     # Total rental sepeda
    rentals_per_hours =("cnt", "mean")      # Rata-rata rental sepeda
)

print(df_rentals_bytimedesc)

st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}<\style>', unsafe_allow_html=True)
image = Image.open("Dashboard/images.png")

col1, col2 = st.columns([0.1,0.9])
with col1 :
    st.image(image, width=200)
    
html_title = """
    <style>
    .title-test {
    font-weight:bold;
    padding:5px;
    border-radius:6px;
    }
    </style>
    <center><h1 class="title-test">Bike Rental Behaviour Dashboard</h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html=True)
    
col3, col4,col5 = st.columns([0.1,0.45,0.45])

with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last Update : \n {box_date}")

with col4:
    fig1 = px.bar(df_rentals_byseason,x ='total_rentals',y='season_desc',title= 'Total Bike Rentals by Season',template='gridon',height=500,hover_data=['total_rentals'],labels={"total_rentals":"Total Rentals","season_desc":"Season"} )
    st.plotly_chart(fig1,use_container_width=True)
    
 
with col5:
    fig2 = px.bar(df_rentals_byweather,x ='total_rentals',y='weather_desc',title= 'Total Bike Rentals by Weather',template='gridon',height=500,hover_data=['total_rentals'],labels={"total_rentals":"Total Rentals","weather_desc":"Weather"} )
    st.plotly_chart(fig2,use_container_width=True)
    
col6, col7 = st.columns([0.1,0.9])

#with col6:
    
with col7:
    fig3 = px.bar(df_rentals_bytimedesc, x ='Time_Desc',y='rentals_per_hours',title= 'Total Bike Rentals by Group Time',template='gridon',height=500,hover_data=['rentals_per_hours'],labels={"rentals_per_hours":"Rental/Hours","Time_Desc":"Group Time"} )
    st.plotly_chart(fig3,use_container_width=True)
