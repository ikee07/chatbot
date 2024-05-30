import os
from dotenv import load_dotenv
from twilio.rest import Client
from chatbot import ask
import openai

load_dotenv()

# Twilio account information
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

# OpenAI API information
openai.api_key = os.getenv("sk-")
completion = openai.Completion()

def send_text(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )

    print("Message sent: ", message.sid)

def get_response(message):
    response = ask(message)
    return response

if __name__ == "__main__":
    while True:
        message = input("Enter a message (type 'exit' to stop): ")
        if message.lower() == 'exit':
            break
        response = get_response(message)
        send_text(response)
