from openai import OpenAI

import os


import random


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def collect_user_context():
    print("Let me get to know your vibe today 🌤️")

    weather = input("1. How’s the weather right now? ")
    place = input("2. Where are you? City? Country side? Work? Home? ")
    mood = input("3. How are you feeling emotionally? ")
    worry = input("4. Is anything bothering you today? ")


    # Create a natural language context
    context = (
        f"The weather is {weather.lower()}. "
        f"They are now at {place.lower()}. "
        f"They are feeling {mood.lower()}. "
        f"Today, they mentioned that '{worry}'."
    )

    return context


def get_inspiring_idea(context):
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
        return idea

    except Exception as e:
        return f"Error getting idea: {str(e)}"


# Run the interaction
print("🌞 Welcome to your Personal Uplifter 🌈\n")
user_context = collect_user_context()
print("\nThinking of something just for you...\n")
idea = get_inspiring_idea(user_context)
print(idea)