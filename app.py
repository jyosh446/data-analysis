import streamlit as st
from PIL import Image
from multiapp import MultiApp
from apps import da1, da2, model, home

image1 = Image.open("images.jpg")
st.set_page_config(
    page_title="Data Analysis",
    page_icon=image1,
    layout = 'wide'
)


apps = MultiApp()

apps.add_app("Home", home.app)
apps.add_app(" Data Analysis on car dataset", da1.app)
apps.add_app("Data Analysis", da2.app)
apps.add_app("Car Predictions", model.app)

# The main app
apps.run()
