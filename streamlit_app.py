import streamlit as st
import joblib

import subprocess
import sys

def install_gdown():
    """Install gdown using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])

# Check if gdown is installed
try:
    import gdown
except ImportError:
    print("gdown is not installed. Installing...")
    install_gdown()
    import gdown  # Now import gdown after installation

# Function to download model from Google Drive
def download_model(file_id, output):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output, quiet=False)

# Download the model file from Google Drive
file_id = 'https://drive.google.com/file/d/13jhgxXZI11GvCz3tbQ56-zi2QuJ0LFFJ/view?usp=sharing'
download_model(file_id, 'model.pkl')  # Download model file

# Load the trained model
model = joblib.load('model.pkl')

# Function for prediction
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



