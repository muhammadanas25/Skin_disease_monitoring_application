import streamlit as st
st.set_page_config(page_title="Dashboard", page_icon="📈")

from datetime import datetime

from db import get_data, GET_GRAPH_DATA


if "logged_in_user" in st.session_state:

    with st.container():
        st.header("Hands")
        query = GET_GRAPH_DATA.format(body_part="Hand", patient_username=st.session_state["logged_in_user"])
        df = get_data(query)
        df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%m-%d-%Y').date())
        st.line_chart(df, x = 'date' , y = 'disorder_percentage')

    with st.container():
        st.header("Face")
        query = GET_GRAPH_DATA.format(body_part="Face", patient_username=st.session_state["logged_in_user"])
        df = get_data(query)
        df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%m-%d-%Y').date())
        st.line_chart(df, x = 'date' , y = 'disorder_percentage')

    with st.container():
        st.header("Legs")
        query = GET_GRAPH_DATA.format(body_part="Leg", patient_username=st.session_state["logged_in_user"])
        df = get_data(query)
        df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%m-%d-%Y').date())
        st.line_chart(df, x = 'date' , y = 'disorder_percentage')

else:
    st.header("Please Login!")