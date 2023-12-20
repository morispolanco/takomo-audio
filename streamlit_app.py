import requests
import time
import streamlit as st

API_KEY = "tk_258c8e8ff4d803a9adad65032fc283d72ccf953cb3910caedba786d420b36e39a2b3e309d529da25c3c2fa3625485947"
ENDPOINT_ID = "62391ec5-cb73-40b0-afa5-9279a7f1060c"

st.title("Transcriptor de audio")

audio_file = st.file_uploader("Sube un archivo de audio")

@st.cache
def transcribe(audio):

  # Transcription request
  
if audio_file is not None:

  try:

    job_response = transcribe(audio_file)
    job_id = job_response.json()['id']

    # Check status loop 

    result = status_response.json()['data']
    transcript = result['transcript']

  except Exception as e:
    st.write(f"Error: {e}")

  else:
    st.write(f"Transcripción: {transcript}")

else:

  st.write("Por favor selecciona un archivo de audio")
