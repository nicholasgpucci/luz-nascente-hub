import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Luz Nascente Hub", page_icon="🌅", layout="centered")

# CSS Predefinitions
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f3ea;
    }

    .link-button {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        max-width: 300px;
        text-align: center;
        padding: 0.8em 1.2em;
        margin: 10px auto;
        background-color: #d4a762;
        color: white !important;
        border-radius: 50px;
        text-decoration: none !important;
        font-size: 18px;
        font-weight: 500;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }

    .link-button:hover {
        background-color: #c19655;
        color: white !important;
    }

    .link-button img {
        margin-right: 10px;
    }

    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo
def image_to_base64(img_path):
    img = Image.open(img_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

img_base64 = image_to_base64("luz_nascente_logo.jpeg")

st.markdown(
    f"""
    <div class="center">
        <img src="data:image/png;base64,{img_base64}" width="200">
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<p style="text-align: center; font-size: 18px; font-weight: normal;">Bem-vindo! Escolha abaixo:</p>',
    unsafe_allow_html=True
)


st.write("---")

# Buttons
st.markdown(
    """
    <a class="link-button" href="https://wa.me/5511941816771" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/WhatsApp_icon.png" width="20">
        Whatsapp
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <a class="link-button" href="https://instagram.com/seuperfil" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" width="20">
        Instagram
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <a class="link-button" href="mailto:contato@luznascente.com" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Mail_%28iOS%29.svg" width="20">
        Contato
    </a>
    """,
    unsafe_allow_html=True
)

st.write("---")

st.markdown(
    """
    <style>
    .footer-text {
        text-align: center;
        font-size: 14px;
        font-weight: normal;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p class="footer-text">Feito com 💛 por Luz Nascente</p>',
    unsafe_allow_html=True
)

