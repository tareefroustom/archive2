import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

st.markdown("""<head>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Titillium Web">
                <style>
                body {font-family: "Titillium Web", sans-serif}
                </style>
                </head>""", unsafe_allow_html=True)

st.image("logo.png")
st.markdown("<h1 style='text-align: center;font-size:40px; color:#676FA3; font-family: Titillium Web'>MIMAS Document Analysis and Management Demo</h1>", unsafe_allow_html=True)

df = pd.read_excel("BR_Title_Mapping_20220104.xlsx")
pr = df.profile_report()

st_profile_report(pr)
