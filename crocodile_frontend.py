import streamlit as st
import pandas as pd
import joblib
from PIL import Image

pipeline = joblib.load("pipeline.pkl")
label_map = joblib.load("label_map.pkl")

inverse_label_map = {v: k for k, v in label_map.items()}

st.set_page_config(page_title="Crocodilian Classifier", layout="centered")
st.markdown("""
    <style>
    .main {background-color: #f0f4f7;}
    .stButton>button {background-color: #4CAF50; color: white; font-weight: bold;}
    .stTextInput>div>input {border: 1px solid #4CAF50;}
    .stSelectbox>div>div {border: 1px solid #4CAF50;}
    </style>
""", unsafe_allow_html=True)

st.title("🦎 Crocodilian Classifier")
st.write("Enter the observed details below to predict the species.")

length = st.number_input("Observed Length (m)", min_value=0.1, max_value=10.0, step=0.1)
weight = st.number_input("Observed Weight (kg)", min_value=0.1, max_value=1000.0, step=0.1)
age_class = st.selectbox("Age Class", ['Adult', 'Subadult', 'Juvenile', 'Hatchling'])
sex = st.selectbox("Sex", ['Unknown', 'Male', 'Female'])
conservation_status = st.selectbox("Conservation Status", [
    'Least Concern', 'Critically Endangered', 'Vulnerable',
    'Data Deficient', 'Endangered'
])
country = st.selectbox("Country", [
    'Other', 'Papua New Guinea', 'Cuba', 'Philippines', 'Australia',
    'Venezuela', 'Malaysia (Borneo)', 'Mexico', 'Congo (DRC)',
    'Indonesia (Papua)', 'Colombia', 'Indonesia (Borneo)', 'Cameroon',
    'Congo Basin Countries', "Côte d'Ivoire", 'Guatemala', 'Belize',
    'Liberia', 'India', 'Sierra Leone', 'Guinea', 'Ghana', 'Nigeria',
    'Central African Republic', 'Pakistan', 'Cambodia', 'Tanzania', 'Mali',
    'Niger', 'Iran (historic)', 'Vietnam', 'Laos', 'Thailand', 'Sudan',
    'Gabon'
])
habitat = st.selectbox("Habitat Grouped", [
    'Other', 'Rivers', 'Swamps', 'Forest Swamps', 'Lakes',
    'Freshwater Wetlands', 'Estuarine Systems', 'Estuaries', 'Mangroves',
    'Flooded Savannas', 'Forest Rivers', 'Reservoirs', 'Small Streams',
    'Shaded Forest Rivers', 'Large Rivers', 'Marshes', 'Freshwater Marshes',
    'Slow Streams'
])

bmi = weight / (length ** 2) if length > 0 else 0

input_dict = {
    "Observed Length (m)": length,
    "Observed Weight (kg)": weight,
    "BMI": bmi,
    "Age Class": age_class,
    "Sex": sex,
    "Conservation Status": conservation_status,
    "Country_grouped": country,
    "Habitat_grouped": habitat
}

if st.button("Predict"):
    input_df = pd.DataFrame([input_dict])
    prediction = pipeline.predict(input_df)[0]
    predicted_label = inverse_label_map.get(prediction, "Unknown")
    st.success(f"🧬 Predicted Species: **{predicted_label}**")
    st.write("### Input Summary")
    st.dataframe(input_df)
    st.write("### Species Image")
    try:
        image_path = f"images/{predicted_label}.jpg"
        image = Image.open(image_path)
        st.image(image, caption=predicted_label, use_container_width=True)
    except:
        st.warning("No image available for this species.")
