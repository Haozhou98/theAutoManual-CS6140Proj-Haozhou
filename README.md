
# the Auto-Manual by Haozhou for CS6140 Project

## Overview

The Auto-Manual project is a practical solution that leverages Optical Character Recognition (OCR), GPT-3.5-turbo, and speech synthesis to assist in diagnosing and providing guidance on faults in industrial equipment. The application focuses on extracting fault messages from human-machine interfaces, using GPT-3.5-turbo to offer maintenance advice, and then employing a voice model to deliver this advice. A demo video was attached.

## Features

- **Image-to-Text Conversion:** Extracts text from images of human-machine interfaces using OCR (via `pytesseract`).
- **AI-Powered Feedback Generation:** Utilizes GPT-3.5-turbo (through `openai` and `langchain` libraries) to generate feedback and guidance based on the extracted text.
- **Text-to-Speech Synthesis:** Converts the generated feedback into speech using Hugging Face's voice model API.
- **Streamlit Integration:** Utilizes Streamlit, an open-source app framework, to create a user-friendly web interface for the AutoManual. It allows users to interact with the OCR and AI models through a GUI.

## Installation

To set up this project, you need to have Python 3.9 installed along with the following dependencies **(Please be strictly following them)**:

- `requests==2.27.1`
- `pytesseract==0.3.13`
- `streamlit==1.29.0`
- `openai==0.28.1`
- `langchain==0.0.248`
- `typing-extensions==4.5.0`

## Usage

1. **Start the Streamlit App:** Make sure to download the attached test image as an uploaded file, and run the main script to start the Streamlit application.
   ```bash
   streamlit run AutoManual.py
   ```
2. **Upload an Image:** Use the test image of the human-machine interface showing a fault message.
3. **View and Hear the Feedback:** The web app will display the extracted fault message, generate and display feedback, and synthesize this feedback into speech.

## Configuration

- Use your own `HUGGINGFACE_API_KEY` and `OPENAI_API_KEY` for accessing the respective APIs.

## Acknowledgments

This project is part of the CS6140 course and was developed by Haozhou Zhou. It showcases the integration of OCR, advanced language models, and speech synthesis in a practical application.
