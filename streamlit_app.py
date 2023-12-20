import requests
import time
import streamlit as st

API_KEY = "tk_258c8e8ff4d803a9adad65032fc283d72ccf953cb3910caedba786d420b36e39a2b3e309d529da25c3c2fa3625485947"
BASE_URL = "https://api.takomo.ai/"

st.title("Transcriptor de audio")

audio_file = st.file_uploader("Sube un archivo de audio")

@st.cache
def transcribe(audio):
  files = {"audio": audio}
  headers = {"Authorization": f"Bearer {API_KEY}"}

  response = requests.post(BASE_URL + "transcription", 
                           files=files, 
                           headers=headers)
  return response

if audio_file:
  try:
    job_response = transcribe(audio_file)
    job_id = job_response.json()['id']

    status = None
    while status != 'completed':
      status_response = requests.get(BASE_URL + f"transcription/{job_id}")  
      status = status_response.json()['status']
      st.write(f"Procesando... Status: {status}")
      time.sleep(5)

    result = status_response.json()['data']
    transcript = result['transcript']

  except Exception as e:
    st.write(f"Error: {e}")

  else:
    st.write(f"Transcripción: {transcript}")
