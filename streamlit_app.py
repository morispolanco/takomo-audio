import streamlit as st
import requests
import io
import time

API_KEY = "tk_258c8e8ff4d803a9adad65032fc283d72ccf953cb3910caedba786d420b36e39a2b3e309d529da25c3c2fa3625485947"
ENDPOINT = "https://api.endpoint"

st.title("Transcriptor")

audio = st.file_uploader("Sube audio")

if audio:

  files = {"audio": io.BytesIO(audio.read())}
  headers = {"Authorization": f"Bearer {API_KEY}"}

  try:
    response = requests.post(ENDPOINT, files=files, headers=headers)
    response.raise_for_status()
    response_data = response.json()

  except Exception as e:
    st.write(f"Error en la petición: {e}")

  else:
    
    job_id = response_data["id"]

    while True:

      status = requests.get(f"{ENDPOINT}/{job_id}").json()

      if status["status"] == "completed":
        break

      st.write("Procesando...")
      time.sleep(5)

    try:  
      transcript = status["data"]["transcript"]
    except KeyError:
      st.write("Error en transcripción")
    else:
      st.write(f"Transcripción: {transcript}")
