import langchain_helper as lch
import streamlit as st

# Sets the title of the Streamlit web application to "Pet Name Generator".
st.title("Pet Name Generator")

# Creates a dropdown select box in the sidebar for choosing the type of pet, with options for Cat, Dog, Cow, and Hamster.
animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))
if animal_type == "Cat":
    pet_color = st.sidebar.text_area(label = "What color is your cat?", max_chars = 15)

if animal_type == "Dog":
    pet_color = st.sidebar.text_area(label = "What color is your dog?", max_chars = 15)

if animal_type == "Cow":
    pet_color = st.sidebar.text_area(label = "What color is your cow?", max_chars = 15)

if animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label = "What color is your hamster?", max_chars = 15)
