import streamlit as st
from openai import OpenAI
import os
import random
from datetime import datetime

# Initialize OpenAI client
if not os.getenv("OPENAI_API_KEY"):
    st.error("Please set OPENAI_API_KEY environment variable")
    st.stop()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit page settings
st.set_page_config(page_title="Daily Uplift", page_icon="🌈")

st.title("🌞 Daily Uplift")
st.subheader("Let me, with a little help from AI, brighten your day")

# Initialize session state for current idea
if 'current_idea' not in st.session_state:
    st.session_state.current_idea = None
if 'show_idea' not in st.session_state:
    st.session_state.show_idea = False
if 'feedback' not in st.session_state:
    st.session_state.feedback = None

# Get current local time and day
now = datetime.now()
current_time = now.strftime("%H:%M")
current_day = now.strftime("%A")  # e.g. "Monday"
time_of_day = (
    "morning" if 5 <= now.hour < 11 else
    "afternoon" if 11 <= now.hour < 18 else
    "evening" if 18 <= now.hour < 22 else
    "night"
)

# Prompt templates with different tones and types of suggestions
prompt_templates = [
    "Speak directly to your friend and offer a creative and simple action to lift their mood:",
    "Talk to your friend with warmth and suggest a light-hearted and slightly unexpected idea to feel more joyful:",
    "Give your friend a thoughtful, cheerful tip to brighten their moment—speak as if you're writing them a short, caring message:",
    "Use your imagination to directly tell your friend how they can boost their spirits today:",
    "You're a warm, encouraging friend. Give your friend a small, delightful suggestion to spark joy:",
    "Offer something delightful and uncommon, and speak directly to your friend as if you're chatting with them:",
    f"Give your friend a {time_of_day}-appropriate spark of joy in the form of a metaphor, small ritual, or sensory experience:",
    "Use a mindful, calming approach to suggest an idea that helps your friend reflect and feel grounded:",
    f"Offer a light-hearted, {time_of_day}-appropriate humorous idea that would bring a smile to your friend's face:"
]

# User input
weather = st.text_input("1. How's the weather right now?")
places = st.text_input("2. Where are you? (At work or at home, in the city or countryside?)")
mood = st.text_input("3. How are you feeling emotionally?")
worry = st.text_input("4. Is anything bothering you today?")

if st.button("Get My Inspiring Idea 🏄‍♂️"):
    if not all([weather, places, mood, worry]):
        st.warning("Please fill in all fields to get your idea")
    else:
        with st.spinner("Thinking..."):
            context = (
                f"It's {current_day} {time_of_day} (local time). "
                f"The weather is {weather.lower()}. "
                f"They are now at {places.lower()}. "
                f"They are feeling {mood.lower()}. "
                f"Today, they mentioned: '{worry}'."
            )

            # Randomly choose a template
            prompt = random.choice(prompt_templates)

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": (
                            f"You are a warm, kind, emotionally intelligent friend. "
                            f"Speak directly to your friend (the user) with compassion. "
                            f"Consider it's {current_day} {time_of_day} in their location. "
                            f"Use the information they shared to give a supportive and uplifting idea or message. "
                            f"Keep it short, imaginative, and emotionally resonant."
                        )},
                        {"role": "user", "content": (
                            f"{prompt}\n\n"
                            f"Here's what your friend shared with you:\n"
                            f"- Current time: {current_day} {time_of_day}\n"
                            f"- Weather: {weather}\n"
                            f"- Location: {places}\n"
                            f"- Mood: {mood}\n"
                            f"- Worry: {worry}\n\n"
                            f"Based on this, what would you say to cheer them up?"
                        )}
                    ],
                    max_tokens=200,
                    temperature=1.0
                )

                st.session_state.current_idea = response.choices[0].message.content.strip()
                st.session_state.show_idea = True
                st.session_state.feedback = None

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# Display current idea if available
if st.session_state.show_idea and st.session_state.current_idea:
    st.success(f"🌿 Here's your idea:\n\n{st.session_state.current_idea}")

    # Rating buttons
    col1, col2 = st.columns(2)

    def give_feedback(rating):
        st.session_state.feedback = rating
        # Saving ideas
        # if rating == "liked":
        #     try:
        #         with open("ideas.txt", "a", encoding="utf-8") as f:
        #             f.write(st.session_state.current_idea + "\n---\n")
        #     except Exception as e:
        #         st.error(f"Couldn't save your idea: {e}")

    with col1:
        if st.button("👍 I liked it"):
            give_feedback("liked")

    with col2:
        if st.button("👎 Not for me"):
            give_feedback("disliked")

# Show feedback message if available
feedback = st.session_state.get("feedback", None)

if feedback == "liked":
    st.success("I'm really happy to hear that! :)")
elif feedback == "disliked":
    st.warning("No worries! Try another idea.")


# to start run in terminal: streamlit run inspiration_app.py