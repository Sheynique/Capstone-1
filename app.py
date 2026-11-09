from huggingface_hub import hf_hub_download
import joblib
import streamlit as st

st.title("🚀 Sliding Threshold Model App")


# 1. Download and load your model from Hugging Face
@st.cache_resource
def load_models():
  model_path = hf_hub_download(
      repo_id="Shey77/my-large-model", filename="sliding_threshold_models.pkl"
  )
  return joblib.load(model_path)


with st.spinner("Downloading and loading model from Hugging Face..."):
  models = load_models()

st.success("✅ Model loaded successfully!")

# Display what is inside the .pkl file so we can see its structure
st.write("### Model Structure / Keys:")
st.write(type(models))
if isinstance(models, dict):
  st.write("Dictionary keys:", list(models.keys()))
