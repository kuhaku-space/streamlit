import streamlit as st

st.button("button")
st.selectbox("selectbox", ("select1", "select2"))
st.multiselect("multiselectbox", ("select1", "select2"))
st.radio("radiobutton", ("radio1", "radio2"))
st.sidebar.text_input("text input")
st.sidebar.text_area("text area")
st.sidebar.slider("slider", 0, 100, 50)
st.sidebar.file_uploader("Choose file")
