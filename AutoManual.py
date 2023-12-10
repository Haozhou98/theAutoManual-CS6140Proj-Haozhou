import pytesseract
import requests
import streamlit as st
from PIL import Image
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

# Constants
HUGGINGFACE_API_KEY = "YOUR_HUGGINGFACE_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Initialize OpenAI Chat Model
openai_chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=200, openai_api_key=OPENAI_API_KEY)

def extract_text_from_image(image_url):
    """
    Extracts text from the given image URL using OCR (Optical Character Recognition).

    Args:
    image_url (str): The URL of the image.

    Returns:
    str: The extracted text from the image.
    """
    image = Image.open(image_url)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def generate_gpt_feedback(fault_info):
    """
    Generates feedback for a given fault information using GPT3.5-turbo.

    Args:
    fault_info (str): The fault information to generate feedback on.

    Returns:
    str: The generated feedback from GPT.
    """
    template = """
    You are a Industry 4.0 expert from FESTO Inc. You are also a cyber-physical system factory savvy and know everything about the FESTO Didactic products. You are patient and good at answering questions and providing guidance based on any given fault and error messages from the FESTO Didactic equipment.

    CONTEXT: {fault_info}
    FEEDBACK:
    """
    prompt = PromptTemplate(template=template, input_variables=["fault_info"])
    troubleshooting_chain = LLMChain(llm=openai_chat_model, prompt=prompt, verbose=True)
    feedback = troubleshooting_chain.predict(fault_info=fault_info)
    print(feedback)
    return feedback

def synthesize_speech(feedback, api_key):
    """
    Synthesizes speech from the given text feedback using Hugging Face's API.

    Args:
    feedback (str): The text feedback to be converted into speech.
    api_key (str): The API key for Hugging Face.

    Returns:
    None: Writes the audio to a file under the same directory with the name of 'audio.flac'
    """
    api_url = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {api_key}"}

    payload = {"inputs": feedback}
    response = requests.post(api_url, headers=headers, json=payload)

    with open('audio.flac', 'wb') as file:
        file.write(response.content)

def main():
    """
    The main function to run the Streamlit app.
    """
    st.title("The 'Auto-Manual' by Haozhou for CS6140 Project")
    uploaded_image = st.file_uploader("Upload a PNG image", type=["png"])

    if uploaded_image is not None:
        display_uploaded_image(uploaded_image)
        process_and_display_feedback(uploaded_image)

def display_uploaded_image(uploaded_image):
    """
    Displays the uploaded image in the Streamlit app.

    Args:
    uploaded_image: The uploaded image file.

    Returns:
    None: Displays the image in the app.
    """
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

def process_and_display_feedback(uploaded_image):
    """
    Processes the uploaded image to extract fault information, generate feedback, and synthesize speech.

    Args:
    uploaded_image: The uploaded image file.

    Returns:
    None: Displays the extracted information and feedback in the app.
    """
    fault_info = extract_text_from_image(uploaded_image)
    feedback = generate_gpt_feedback(fault_info)
    synthesize_speech(feedback, HUGGINGFACE_API_KEY)

    with st.expander("Fault/Error Message"):
        st.write(fault_info)
    with st.expander("AutoManual Feedback"):
        st.write(feedback)
    st.audio('audio.flac')

if __name__ == '__main__':
    main()
