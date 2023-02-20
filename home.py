import streamlit as st

def home_app():
    st.title("Car prediction app")
    st.image("data/welcome.jpg")
    st.text(
        """
        This web app allows a user to predict the prices of a car using
        engine size, horse power, dimensions and the drive wheel tyre
        """
    )
