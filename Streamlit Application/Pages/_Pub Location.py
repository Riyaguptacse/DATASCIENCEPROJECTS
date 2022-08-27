#import requirements
import numpy as np
import pandas as pd
import streamlit as st
import Home

#displaing the information
st.title("PUB Location")
df = pd.read_csv('pub.csv')
btn_map = st.button("Display Map ")

if btn_map==True:
    st.map(df)

title_alignment="""
<style>
#pub-location {
  text-align: center
  
}
</style>
"""
title_color="""
<style>
#pub-location {
  color:Black
  
}
</style>
"""
title_font="""

<style>
#pub-location {
  font-family: Brush Script MT, monospace
  
}
</style>
"""
st.markdown(title_color, unsafe_allow_html=True)
st.markdown(title_alignment, unsafe_allow_html=True)
st.markdown(title_font, unsafe_allow_html=True)

st.header("Select a Local Authority")
data_sel= df.local_authority.unique()
#choosing a local authority
optn = st.selectbox(
    'Select a Local Authority',
     data_sel)

'You selected: ', optn

#displaying the map for particular local authority
button_click= st.button('Find Now')
if button_click==True: 
    res= df[df['local_authority']==optn]
    count=res.shape[0]
    st.write("Number of Pubs in this area is:",count)
    res=res[['latitude','longitude']]
    st.map(res)
    st.markdown('_Its displaying all the pubs in the area that you selected_')