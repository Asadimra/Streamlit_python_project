import streamlit as st

#image
st.image("computer.png")
# title
st.title("Welcome to my Website")

#header
st.header("Machine learing")
#sub header
st.subheader("linear information")

# to give information
st.info("Inforamtion detail of user ")

# warning message
st.warning("come on time otherwise i will markes absent")

# Error message
st.error("WRONG PASSWORD")

#sucess message 
st.success("Congralution ")

# write message
st.write("Employee name")
st.write(range (20))

# Markdown
st.markdown("# ASAD")
st.markdown("## ASAD")
st.markdown("### ASAD")
st.markdown(":moon:")
st.markdown(":star:")

# text message
st.text("I am a text message")

# to write a caption
st.caption("caption is here")

# to display a mathematical equation
st.latex('''a+b x^2 + c''')

# Widget
st.checkbox("submit")

#button
st.button("click")

# radio widget
st.radio("pick your gender",["male","female"])

#select box
st.selectbox("pick up your courses",["wpl","ui","cybersecurity"])

#multi select
st.multiselect("choose your department",["content","sales","marketing"])

#select slider
st.select_slider("Rating",["excellent","good","bad"])

#slider
st.slider("enter your number",0,100)

#number input
st.number_input("pick a number",0,100)

#text input
st.text_input("enter your email")

#date input
st.date_input("opening caremony")

#time input
st.time_input("select th time")

#text area
st.text_area("give your comments")

#file upload
st.file_uploader("upload the file here")

st.color_picker("color")

st.progress(80)

#ballons
# st.balloons()

# side bar
st.sidebar.title("Welcome to my website")
st.sidebar.text_input("Enter your email")
st.sidebar.text_input("Enter your password")
st.sidebar.button("submit")


# Data visualization
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.title("Bar chart")
st.bar_chart(data)

st.title("line chart")
st.line_chart(data)

st.title("Area chart")
st.area_chart(data)

