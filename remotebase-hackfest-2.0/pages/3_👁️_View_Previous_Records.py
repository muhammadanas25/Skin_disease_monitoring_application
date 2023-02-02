import streamlit as st
st.set_page_config(page_title="View Previous Record", page_icon="👁️")
from PIL import Image

if "logged_in_user" in st.session_state:

    body_part = st.selectbox(
        'Select Body Part',
        ('Face', 'Hands', 'Legs'))

    date = st.date_input("Date")
   

else:
    st.header("Please Login!")


