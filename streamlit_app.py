import streamlit as st
import requests
from pydub import AudioSegment
import tempfile
import os

# Configurar la ubicación de FFmpeg
from pydub import AudioSegment

AudioSegment.converter = "/usr/bin/ffmpeg"

def transcribe_and_improve_voice(api_key, audio_data):
    # URL de la API Whisper
    api_url = "https://api.whisper.ai/your_whisper_api_endpoint"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio_path = temp_audio.name
        audio_data.export(temp_audio_path, format="wav")

    with open(temp_audio_path, "rb") as audio_file:
        files = {"audio_file": audio_file}
        response = requests.post(api_url, files=files, headers=headers)

    os.remove(temp_audio_path)

    if response.status_code == 200:
        result = response.json()
        return result.get("transcription", "No transcripción disponible")
    else:
        return f"Error en la solicitud: {response.status_code}"

def main():
    st.title("Transcripción y Mejora de Notas de Voz con Streamlit")

    audio_file = st.file_uploader("Cargar archivo de audio (m4a)", type=["m4a"])
    api_key = st.text_input("Introduce tu API Key de Whisper:")

    if st.button("Transcribir y Mejorar"):
        if not audio_file or not api_key:
            st.warning("Por favor, carga un archivo de audio en formato m4a y introduce la API Key de Whisper.")
        else:
            st.info("Transcribiendo y mejorando... Esto puede tomar un tiempo.")
            
            audio_data = AudioSegment.from_file(audio_file, format=audio_file.name.split('.')[-1])
            result = transcribe_and_improve_voice(api_key, audio_data)
            
            st.success(f"Transcripción mejorada:\n\n{result}")

if __name__ == "__main__":
    main()
