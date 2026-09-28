import streamlit as st
st.title("job application")
st.header("--RESUME--")
st.subheader("DETAILS:")
st.text_input("NAME")
st.text_input("ADDRESS")
st.text_input("PHONE NO")
st.text_input("MAIL")

st.divider()
st.header("SUBJECT")
st.subheader("To pursue as AI engineer")
st.file_uploader("upload a resume")
st.color_picker("choose color","#19b9dd")
st.header("BODY")
st.text_area("my name is pranavi." \
"i want to pursue ai engineer " \
"i have completed my b-tech in mrecw in aiml course,i have eduactes in the python,agentic ai,prompting,llms" \
"")