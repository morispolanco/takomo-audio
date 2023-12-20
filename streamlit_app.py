import streamlit as st
import requests
import io
import time

API_KEY = "tk_258c8e8ff4d803a9adad65032fc283d72ccf953cb3910caedba786d420b36e39a2b3e309d529da25c3c2fa3625485947"
ENDPOINT_URL = "https://api.takomo.ai/endpoint"

st.title("Transcriptor de audio")

audio_file = st.file_uploader("Sube un archivo")

if audio_file:

  audio = io.BytesIO(audio_file.read())

  files = {"audio": audio}
  headers = {"Authorization": f"Bearer {API_KEY}"}

  response = requests.post(ENDPOINT_URL, files=files, headers=headers)

  job_id = response["id"]

  while True:

    status_response = requests.get(f"{ENDPOINT_URL}/{job_id}")

    if status_response["status"] == "completed":
      break

    st.write("Procesando...")
    time.sleep(5)

  data = status_response["data"]

  try:
    transcript = data["transcript"]
  except KeyError:
    st.write("Error en la transcripción")
  else:
    st.write(f"Transcripción: {transcript}")
