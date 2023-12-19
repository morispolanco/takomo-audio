import streamlit as st
import requests

def transcribe_and_improve_voice(api_key, audio_url):
    api_url = "https://api.takomo.ai/62391ec5-cb73-40b0-afa5-9279a7f1060c"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer tk_258c8e8ff4d803a9adad65032fc283d72ccf953cb3910caedba786d420b36e39a2b3e309d529da25c3c2fa3625485947"
    }

    payload = {
        "audio_url": audio_url
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result.get("transcription", "No transcripción disponible")
    else:
        return f"Error en la solicitud: {response.status_code}"

def main():
    st.title("Transcripción y Mejora de Notas de Voz con Streamlit")

    audio_url = st.text_input("Introduce la URL del archivo de audio:")
    api_key = st.text_input("Introduce tu API Key:")

    if st.button("Transcribir y Mejorar"):
        if not audio_url or not api_key:
            st.warning("Por favor, introduce la URL del archivo de audio y la API Key.")
        else:
            st.info("Transcribiendo y mejorando... Esto puede tomar un tiempo.")
            result = transcribe_and_improve_voice(api_key, audio_url)
            st.success(f"Transcripción mejorada:\n\n{result}")

if __name__ == "__main__":
    main()
