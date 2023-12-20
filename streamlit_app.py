import streamlit as st
import requests
import io

API_KEY = "tk_258c8e8ff4d803a9adad65032fc283d72ccf953cb3910caedba786d420b36e39a2b3e309d529da25c3c2fa3625485947"
ENDPOINT_URL = "https://api.takomo.ai/62391ec5-cb73-40b0-afa5-9279a7f1060c"

st.title("Transcriptor de audio")

audio_file = st.file_uploader("Sube un archivo de audio")

if audio_file:

  try:

    audio = io.BytesIO(audio_file.read())

    files = {"audio": audio}

    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.post(ENDPOINT_URL, 
                             files=files,
                             headers=headers)

  except Exception as e:
    st.write(f"Error en la petición: {e}")

  else:

    try:
      data = response.json()
    except Exception:
      st.write("Error al procesar la respuesta")
    else:

      st.write("Respuesta de la API:")
      st.write(data)

      try:
        transcript = data["transcript"]
      except KeyError:
        st.write("Respuesta no contiene campo transcript")  
      else:
        st.write(f"Transcripción: {transcript}")
st.title("Transcriptor de audio")

audio_file = st.file_uploader("Sube un archivo de audio")

if audio_file:

  try:

    audio = io.BytesIO(audio_file.read())

    files = {"audio": audio}

    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.post("https://api.takomo.ai/endpoint",
                             files=files,
                             headers=headers)

  except Exception as e:
    st.write(f"Error en la petición: {e}")

  else:

    data = response.json()

    st.write("Respuesta de la API:")
    st.write(data)

    try:
      transcript = data["transcript"]
    except KeyError:
      st.write("Respuesta no contiene campo transcript")
    else:  
      st.write(f"Transcripción: {transcript}")
