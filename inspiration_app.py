import streamlit as st
from openai import OpenAI
import os

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
                    {"role": "system", "content": "You are an inspiring friend who gives creative, cheerful suggestions to help someone feel uplifted."},
                    {"role": "user", "content": f"{context} Suggest one small but inspiring idea or action to help me feel better right now."}
                ],
                max_tokens=200,
                temperature=1.0
            )

            idea = response.choices[0].message.content.strip()
            st.success(f"Here’s your idea ✨\n\n{idea}")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# to start run in terminal: streamlit run inspiration_app.py
