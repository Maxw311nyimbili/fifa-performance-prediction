import streamlit as st

import subprocess
import sys

def install_packages():
    """Install required packages using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown", "joblib"])
    except subprocess.CalledProcessError as e:
        print(f"Error during package installation: {e}")
        sys.exit(1)  # Exit the script if installation fails

# Check if packages are imported
def check_import(package_name):
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

if not check_import("gdown") or not check_import("joblib"):
    print("gdown or joblib is not installed. Installing...")
    install_packages()

# Now import gdown and joblib after installation
import gdown
import joblib

# --------------------------------------------------------------------------

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



