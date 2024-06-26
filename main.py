import langchain_helper as lch
import streamlit as st

# Sets the title of the Streamlit web application to "Pet Name Generator".
st.title("Pet Name Generator")

# Creates a dropdown select box in the sidebar for choosing the type of pet, with options for Cat, Dog, Cow, and Hamster.
user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))
if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label = "What color is your cat?", max_chars = 15)

if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label = "What color is your dog?", max_chars = 15)

if user_animal_type == "Cow":
    pet_color = st.sidebar.text_area(label = "What color is your cow?", max_chars = 15)

if user_animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label = "What color is your hamster?", max_chars = 15)

# Displays the generated response (suggested pet names) in the main area of the Streamlit app.
if pet_color:
    response= lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])