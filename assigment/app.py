import streamlit as st
from agent import shopping_agent  

st.title("AI Shopping Assistant")
user_input = st.text_input("Enter your shopping request:")
if user_input:
    response = shopping_agent(user_input)
    st.write(response)
