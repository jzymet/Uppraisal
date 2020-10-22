import streamlit as st
import numpy as np
import pandas as pd

st.title("Selling your MacBook Pro?")

#img = Image.open("macbook.jpg")
#img.show()

yearintitle = 0
sizeintitle = 0
memoryintitle = 0
title = st.text_input("Put the title of your listing here:")

hasdescription = 0
if st.checkbox('Add description?'):
    hasdescription = 1
    description = st.text_area("Have at it:")
    
specsdict = {
    "year": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    "size": [13, 14, 15, 16, 17],
    "memory": [120, 250, 500, 750, 1000]}

option1 = st.selectbox(
    "What year was your MacBook manufactured?", specsdict['year'])

option2 = st.selectbox(
    "What's its screen size?", specsdict['size'])

option3 = st.selectbox(
    "What about memory (in GB)?", specsdict['memory'])

if str(option1) in title: yearintitle = 1
if str(option2) in title: sizeintitle = 1
if str(option3) in title: memoryintitle = 1

if title == "" and option1 == 2011:
    predprice = 0
else:
    predprice = -273800 + 224 + 135*option1 + 147*option2 + 0.6*option3 + 63*sizeintitle + 10*memoryintitle + 18*hasdescription
"Predicted price for your MacBook: $", predprice

"ADVICE"
if str(option2) not in title:
    "Put the screen size into the title—I predict that it'll sell for $63 more if you do!"

if str(option3) not in title:
    "Put the memory, in GB, into the title—I predict that it'll sell for $10 more if you do."

if hasdescription == 0:
    "You didn't make a description! I predict that the MacBook will sell for $18 more if you include one."

"Also, aim for a fleshed out description: buyers like it when they're longer."
