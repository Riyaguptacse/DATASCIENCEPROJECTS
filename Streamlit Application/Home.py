#import requirements
import streamlit as st
import pandas as pd
import numpy as np

#reading dataset
df=pd.read_csv('pub.csv')

st.set_page_config(
     page_title="Streamlit App",
     page_icon=":shark:",
     layout="wide"
 )
st.sidebar.success("Select the required option")
#title alignment and color


st.title("Welcome to Open Pub Application")
title_alignment="""
<style>
#welcome-to-open-pub-application {
  text-align: center
  
}
</style>
"""
title_color="""
<style>
#welcome-to-open-pub-application {
  color:Black
  
}
</style>
"""
title_font="""

<style>
#welcome-to-open-pub-application {
  font-family: Brush Script MT, monospace
  
}
</style>
"""
st.markdown(title_color, unsafe_allow_html=True)
st.markdown(title_alignment, unsafe_allow_html=True)
st.markdown(title_font, unsafe_allow_html=True)


st.header("TIME FOR SOME DRINKS...LET'S ENJOY!")



st.text("The data describes UK pub names along with their addresses, positions, and local authority.")
df[['latitude', 'longitude']]=df[['latitude', 'longitude']].apply(pd.to_numeric, axis = 1)
data_sel= df.local_authority.unique()
pub= "Total number of PUBS: "+str(df.shape[0])
auth="Total number of PUBS Local Authority: " +str(data_sel.shape[0])
latitude_range= "Latitude Range of Data: "+str(df['latitude'].min())+" to "+str(df['latitude'].max())
longitude_range= "Longitude Range of Data: "+str(df['longitude'].min())+" to "+str(df['longitude'].max())
st.dataframe(df.head())
st.subheader('Find the Statistics information of the pub dataset')
stat = st.button('Describe')

if stat==True:
    st.dataframe(df.describe())
else:
    st.text('')

st.subheader(pub)
st.subheader(auth)
st.subheader(latitude_range)
st.subheader(longitude_range)

