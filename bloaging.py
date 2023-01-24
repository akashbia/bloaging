# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:39:26 2022

@author: HP
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

st.header("bloaging with spyder")
st.subheader("bloaging page with information")
st.write("i am a bloger")
st.button("re_run")

option = st.sidebar.selectbox("select application",("facebook","instagram", "linkedin", "whatsapp"))

st.image("https://th.bing.com/th/id/OIP.9gArZ5Z2dAG7LqeLyw5OGQHaEK?pid=ImgDet&rs=1")

st.write("here is our first attempt using data to create a table:")
st.write(pd.DataFrame({
    "first column":[1,2,3,4],
    "second column":[10,20,30,40]
    }))

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=("col %d" % i for i in range (20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
    np.random.randn(10,3),
    columns=["a","b","c"])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(100,2),
    columns = ("lat", "lon"))

st.map(map_data)

x = st.slider("x")
st.write(x, "squared is", x*x)

st.text_input("your name", key="name")
st.session_state.name

if st.checkbox("show dataframe"):
     chart_data= pd.DataFrame(
         np.random.randn(20,3),
         columns=["a","b","c"])
     chart_data

df = pd.DataFrame({
    "first column":[1,2,3,4],
    "second column":[10,20,30,40]
    })

option = st.selectbox(
    "which number do you like best?",
    df["first column"])

"you selected:", option

add_slider = st.sidebar.slider(
    "select a range of values",
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
left_column.button("press me!")

with right_column:
    chosen = st.radio(
        "Sorting hat",
        ("gryfindor", "Ravenclaw", "Hufflepuf", "slytherin"))
    st.write(f"you are in {chosen} house!")

    
"starting a long computation..."

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.200)
    
".....and now we\ re done!"

