import streamlit as st
from PIL import Image
from multiapp import MultiApp
from apps import eda1, eda2, model, home

image1 = Image.open("car_eda3.jpg")
st.set_page_config(
    page_title="Data Analysis",
    page_icon=image1,
    layout = 'wide'
)


apps = MultiApp()

apps.add_app("Home", home.app)
apps.add_app("Exploratory Data Analysis on car data by CarDekho", eda1.app)
apps.add_app("Exploratory Data Analysis(EDA)", eda2.app)
apps.add_app("Car Selling Price Prediction", model.app)

# The main app
apps.run()
