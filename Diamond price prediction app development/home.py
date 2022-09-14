import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Diamond App",
    page_icon="💎",
)




st.title("🏠Home Page")
st.header("💠 Welcome to Diamond Price Application 💠 ")
st.sidebar.success("Select a page above.")

################################## DATA LOADING #######################################
df=pd.read_csv("diamonds.csv")

st.subheader('About Diamond')
st.markdown('Diamond is a solid form of the element carbon with its atoms arranged in a crystal structure called diamond cubic. At room temperature and pressure, another solid form of carbon known as graphite is the chemically stable form of carbon, but diamond converts to it extremely slowly. Diamond has the highest hardness and thermal conductivity of any natural material, properties that are used in major industrial applications such as cutting and polishing tools.')

st.subheader("Understanding 4C's")
st.markdown('The value of diamonds depends upon their structure, cut, inclusions (impurity), carats, and many other features. They are graded and certified based on the "four Cs", which are COLOR, CUT, CLARITY, and CARAT. These are the only metrics that are being used to the quality of diamonds and sets the price of the diamond.')

st.subheader("1.CUT")
st.markdown("Cut is the only diamond component not influenced by nature, and Mills considers this the most important of the 4Cs. This factor refers to the quality of the diamond's cut, not the shape or size, and how well the stone is faceted, proportioned, and polished.")



st.subheader("2.COLOR")
st.markdown("Diamond colors fall under a D-Z scale, with D meaning completely colorless (and the most expensive), and Z having a light yellow hue.")



st.subheader("3.CLARITY")
st.markdown("This C involves the number of natural imperfections, called inclusions, present in the diamond, and whether you can see them with the unaided eye.")


st.subheader("4.CARAT")
st.markdown("Carat refers to a measurement of the actual weight of the diamond. According to GIA, one carat converts to 0.2 grams, which is essentially the same weight as a paper clip. Naturally, the larger the carat, the more expensive the diamond.")



