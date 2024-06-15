import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a function for prediction
def predict_player_rating(features):
    return model.predict([features])[0]

# Define the Streamlit app
st.title("Player Rating Prediction")

# Input features from user
attacking_finishing = st.slider("Attacking Finishing", 0, 100)
defending_marking_awareness = st.slider("Defending Marking Awareness", 0, 100)
# Add sliders for other features...
skill_dribbling = st.slider("Skill Dribbling", 0, 100)

# Create a feature list
features = [
    attacking_finishing, defending_marking_awareness, #... other features,
    skill_dribbling
]

# Predict button
if st.button("Predict Rating"):
    rating = predict_player_rating(features)
    st.write(f"Predicted Player Rating: {rating}")

# Run the Streamlit app with `streamlit run app.py`


