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

#Memastikan tipe data pada datetime adalah datetime

datetime_columns = ["dteday"]
df_hour.sort_values(by="dteday", inplace=True)
df_hour.reset_index(inplace=True)
 
for column in datetime_columns:
    df_hour[column] = pd.to_datetime(df_hour[column])

#EDA

min_date = df_hour["dteday"].min()
max_date = df_hour["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://edit.org/img/blog/zer-1024-city-bike-rental-banner-template-editable.webp")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = df_hour[(df_hour["dteday"] >= str(start_date)) & 
                (df_hour["dteday"] <= str(end_date))]

def dfr(main_df):
    df_rentals_byseason = main_df.groupby("season_desc", as_index=False).agg(
        sum_hour=("instant", "nunique"),   # Jumlah hari unik dalam setiap musim
        total_rentals=("cnt", "sum"),      # Total rental sepeda dalam setiap musim
        rentals_per_hours=("cnt", "mean")  # Rata-rata rental sepeda per hari
    ).sort_values(by="total_rentals", ascending=False)
    
    return df_rentals_byseason

def dfw(main_df) : 
    df_rentals_byweather= main_df.groupby(by="weather_desc", as_index=False
    ).agg(
        sum_hour=("instant", "nunique"),   # Jumlah hari unik
        total_rentals=("cnt", "sum"),     # Total rental sepeda
        rentals_per_hours =("cnt", "mean")      # Rata-rata rental sepeda
    ).sort_values(by="total_rentals", ascending=False)
    
    return df_rentals_byweather

def dft(main_df):
    df_rentals_bytimedesc= main_df.groupby(by="Time_Desc", as_index=False
    ).agg(
        sum_hour=("instant", "nunique"),   # Jumlah hari unik
        total_rentals=("cnt", "sum"),     # Total rental sepeda
        rentals_per_hours =("cnt", "mean")      # Rata-rata rental sepeda
    )
    
    return df_rentals_bytimedesc

df1 = dfr(main_df)
df2 = dfw(main_df)
df3 = dft(main_df)

st.header('Bike Rental Behaviour Dashboard :sparkles:')

    
col4,col5 = st.columns(2)

with col4:
    fig1 = px.bar(df1,x ='total_rentals',y='season_desc',title= 'Total Bike Rentals by Season',template='gridon',height=500,hover_data=['total_rentals'],labels={"total_rentals":"Total Rentals","season_desc":"Season"} )
    st.plotly_chart(fig1,use_container_width=True)
    
 
with col5:
    fig2 = px.bar(df2,x ='total_rentals',y='weather_desc',title= 'Total Bike Rentals by Weather',template='gridon',height=500,hover_data=['total_rentals'],labels={"total_rentals":"Total Rentals","weather_desc":"Weather"} )
    st.plotly_chart(fig2,use_container_width=True)
    
with st.container():
    fig3 = px.bar(df3, x ='Time_Desc',y='rentals_per_hours',title= 'Total Bike Rentals by Group Time',template='gridon',height=500,hover_data=['rentals_per_hours'],labels={"rentals_per_hours":"Rental/Hours","Time_Desc":"Group Time"} )
    st.plotly_chart(fig3,use_container_width=True)
