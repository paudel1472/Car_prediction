import streamlit as st


#Import pages
import home
import data
import plots
import predict
import about

#Import other necesary things
from prepro import load_data


#Configure the web page
st.set_page_config(
    page_title = 'Car Price Prediction',
    page_icon = 'car',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

#Create a dict for pages
pages_dict = {
    "Home": home,
    "View Data": data,
    "Visualise Data": plots,
    "Predict": predict,
    "About me": about
}

#Load the datasets
df = load_data()

#Create navbar in sidebar
st.sidebar.title("Navigation")
user_choice = st.sidebar.radio('Go to',("Home","View Data","Visualise Data","Predict","About me"))

#Open the page selected by the user
if (user_choice =="Home"):
    selected_page = pages_dict[user_choice]
    selected_page.home_app()
if (user_choice =="Visualise Data"):
    selected_page = pages_dict[user_choice]
    selected_page.plot_app(df)
if (user_choice =="Predict"):
    selected_page = pages_dict[user_choice]
    selected_page.model_app(df)
if (user_choice =="About me"):
    selected_page = pages_dict[user_choice]
    selected_page.about_app()
if (user_choice =="View Data"):
    selected_page = pages_dict[user_choice]
    selected_page.data_app(df)