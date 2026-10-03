import os
import gradio as gr
from google import genai

# Get API key securely from Hugging Face Secrets
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def chatbot(message, history):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message
    )
    return response.text


demo = gr.ChatInterface(
    fn=chatbot,
    title="My Gemini AI Chatbot",
    description="Ask me anything!",
)

demo.launch()
