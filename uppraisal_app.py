import streamlit as st
import numpy as np
import pandas as pd

st.title("Selling your MacBook Pro?")

#fill in listing title and description

title = st.text_input("Put the title of your listing here:")

if st.checkbox('Add description?'):
    description = st.text_area("Have at it:")

#set checks for whether various specs are mentioned in the title to 0
yearintitle = 0
sizeintitle = 0
memoryintitle = 0

#fill in laptop specs

specsdict = {
    "year": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    "size": [13, 14, 15, 16, 17],
    "memory": [120, 250, 500]}

option1 = st.selectbox(
    "What year was your MacBook manufactured?", specsdict['year'])

option2 = st.selectbox(
    "What's its screen size?", specsdict['size'])

option3 = st.selectbox(
    "What about memory (in GB)?", specsdict['memory'])

#check whether various specs are mentioned in the title

if " " + str(option1) in title: yearintitle = 1
if (" "+str(option2)+" ") or (" "+str(option2)+"in") or (" "+str(option2)+"-in") or (" "+str(option2)+".") or (" "+str(option2)+"'") in title: sizeintitle = 1
if (" "+str(option3)+" ") or (" "+str(option3)+"GB") or (" "+str(option3)+"SSD") in title: memoryintitle = 1

print(yearintitle)
print(sizeintitle)
print(memoryintitle)

#predicted price according to Lasso model coefficients/whether specs are in title

predprice = -255350 + 126*option1 + 139*option2 + 0.6*option3 + (-4)*yearintitle + 42*sizeintitle + 43*memoryintitle
"Predicted price for your MacBook: $", predprice

#advice that dis/appears depending on whether specs are mentioned in title

"ADVICE"

if memoryintitle == 0:
    "Put the memory, in GB, into the title—I predict that it'll sell for $43 more if you do."

if sizeintitle == 0:
    "Put the screen size into the title—I predict that it'll sell for $42 more if you do!"

if yearintitle == 1:
    "This is subtle, but if you leave the year out of the title, I predict it'll sell for around $4 more."

"Also, aim for a fleshed out description that makes you look human! Don't load it up with legalese."
