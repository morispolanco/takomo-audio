import requests
import time
import streamlit as st

API_KEY = "tk_258c8e8ff4d803a9adad65032fc283d72ccf953cb3910caedba786d420b36e39a2b3e309d529da25c3c2fa3625485947"
ENDPOINT_ID = "62391ec5-cb73-40b0-afa5-9279a7f1060c" 

st.title("Transcriptor de audio")

# Transcribe function
def transcribe(audio):

  files = {"audio": audio}

  headers = {"Authorization": f"Bearer {API_KEY}"}

  response = requests.post(f"https://api.takomo.ai/{ENDPOINT_ID}/transcription",
                           files=files,
                           headers=headers)

  return response

# Rest of code...

if audio_file:

  job_response = transcribe(audio_file)

  # Get job ID  
  job_id = job_response.json()['id']

  # Check status loop
  while status != 'completed':

    status_response = requests.get(f"https://api.takomo.ai/{ENDPOINT_ID}/transcription/{job_id}")

    # Process response

  # Return transcript
