import pandas as pd
import streamlit as st
from PIL import Image
import datetime
import plotly.express as px
import plotly.graph_objects as go

df_Season = pd.read_csv("Dashboard/Rental_by_Season.csv")
df_Weather = pd.read_csv("Dashboard/Rental_by_Weather.csv")
df_Daydesc = pd.read_csv("Dashboard/Rental_by_Hourdesc.csv")
df_Peekhours = pd.read_csv("Dashboard/Rental_by_peekhours.csv")

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
    fig1 = px.bar(df_Season,x ='total_rentals',y='season_desc',title= 'Total Bike Rentals by Season',template='gridon',height=500,hover_data=['total_rentals'],labels={"total_rentals":"Total Rentals","season_desc":"Season"} )
    st.plotly_chart(fig1,use_container_width=True)
    
 
with col5:
    fig2 = px.bar(df_Weather,x ='total_rentals',y='weather_desc',title= 'Total Bike Rentals by Weather',template='gridon',height=500,hover_data=['total_rentals'],labels={"total_rentals":"Total Rentals","weather_desc":"Weather"} )
    st.plotly_chart(fig2,use_container_width=True)
    
col6, col7,col8 = st.columns([0.1,0.3,0.6])

#with col6:
    
with col7:
    fig3 = px.pie(df_Daydesc, names ='day_desc',values='rentals_per_hours',title= 'Total Bike Rentals by Day')
    st.plotly_chart(fig3,use_container_width=True)
    
with col8:
    fig4 = px.line(df_Peekhours, x ='hr',y='peek_hours_rental', title= "Peek Hours Rental on Fall Season",labels={"hr":"Hours Time","peek_hours_rental":"Rental per Hours"})
    st.plotly_chart(fig4,use_container_width=True)
