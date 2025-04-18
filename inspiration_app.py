import streamlit as st
from openai import OpenAI
import os

import random

prompt_templates = [
    "Given the following context, suggest a quirky, playful idea to lift someone's mood:",
    "Suggest a creative and slightly unexpected action that can help someone feel more joyful:",
    "From the details below, craft a thoughtful but light-hearted tip to brighten their day:",
    "Use the context to come up with an imaginative way to boost someone's spirits:",
    "Give a poetic or metaphorical suggestion that inspires a moment of joy:"
]

prompt = random.choice(prompt_templates)

# Set your API key securely
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Daily Uplift", page_icon="🌈")

st.title("🌈 Daily Uplift")
st.subheader("Let me create a cheerful idea just for you ")


# User input (Streamlit-style)
weather = st.text_input("1. How’s the weather right now?")
places = st.text_input("2. Where are you? (City? Countryside? Work? Home?)")
mood = st.text_input("3. How are you feeling emotionally?")
worry = st.text_input("4. Is anything bothering you today?")

if st.button("✨ Get My Inspiring Idea"):
    with st.spinner("Thinking..."):
        context = (
            f"The weather is {weather.lower()}. "
            f"They are now at {places.lower()}. "
            f"They are feeling {mood.lower()}. "
            f"Today, they mentioned: '{worry}'."
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "You are an inspiring friend who gives creative, cheerful, and personalized suggestions to "
                        "help someone feel uplifted."
                        "Avoid repeating generic advice like 'go for a walk', 'breathe deeply', or suggesting places "
                        "like a balcony or garden,"
                        "as they may not have access to them. Instead, offer imaginative, cozy, or indoor-friendly "
                        "ideas that feel warm and encouraging."
                    )},
                    {"role": "user", "content": f"{context}. {prompt}"}
                ],
                max_tokens=200,
                temperature=1.1
            )

            idea = response.choices[0].message.content.strip()
            st.success(f"✨ Here’s your idea \n\n{idea}")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# to start run in terminal: streamlit run inspiration_app.py
