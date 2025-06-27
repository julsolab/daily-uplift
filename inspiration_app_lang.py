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

# Optimized language configurations using arrays
LANGUAGES = {
    'en': {
        'name': 'English',
        'flag': '🇺🇸',
        'ai_name': 'English',
        'title': '🌞 Daily Uplift',
        'subtitle': 'Let me, with a little help from AI, brighten your day',
        'questions': [
            "How's the weather right now?",
            "Where are you? (At work or at home, in the city or countryside?)",
            "How are you feeling emotionally?",
            "Is anything bothering you today?"
        ],
        'button': 'Get My Inspiring Idea 🏄‍♂️',
        'fill_warning': 'Please fill in all fields to get your idea',
        'thinking': 'Thinking...',
        'idea_prefix': '🌿 Here\'s your idea:',
        'feedback': ['👍 I liked it', '👎 Not for me'],
        'feedback_responses': [
            'I\'m really happy to hear that! :)',
            'No worries! Try another idea.'
        ],
        'language_label': 'Choose Language',
        'instructions': [
            '🚀 How to use:',
            'Choose your language at the top',
            'Fill in the four questions',
            'Get your personalized uplifting idea!'
        ]
    },
    'ru': {
        'name': 'Русский',
        'flag': '🇷🇺',
        'ai_name': 'Russian',
        'title': '🌞 Ежедневное вдохновение',
        'subtitle': 'Позвольте нам с ИИ поднять вам настроение',
        'questions': [
            "Какая сейчас погода?",
            "Где вы сейчас (на работе, дома, в городе, на даче...)?",
            "Как настроение?",
            "Что-то беспокоит вас?"
        ],
        'button': 'Вдохновиться 🏄‍♂️',
        'fill_warning': 'Пожалуйста, заполните все поля',
        'thinking': 'Думаю...',
        'idea_prefix': '🌿 Вот ваша идея:',
        'feedback': ['👍 Мне понравилось', '👎 Не для меня'],
        'feedback_responses': [
            'Я очень рада! :)',
            'Ага. Попробуйте другую идею?'
        ],
        'language_label': 'Выберите язык',
        'instructions': [
            '🚀 Как использовать:',
            'Выберите язык вверху',
            'Заполните четыре вопроса',
            'Получите персональную вдохновляющую идею!'
        ]
    },
    'de': {
        'name': 'Deutsch',
        'flag': '🇩🇪',
        'ai_name': 'German',
        'title': '🌞 Tägliche Inspiration',
        'subtitle': 'Lass mich, mit ein wenig Hilfe von KI, deinen Tag erhellen',
        'questions': [
            "Wie ist das Wetter gerade?",
            "Wo bist du? (Bei der Arbeit oder zu Hause, in der Stadt oder auf dem Land?)",
            "Wie fühlst du dich emotional?",
            "Beschäftigt dich heute etwas?"
        ],
        'button': 'Meine inspirierende Idee bekommen 🏄‍♂️',
        'fill_warning': 'Bitte fülle alle Felder aus, um deine Idee zu erhalten',
        'thinking': 'Denke nach...',
        'idea_prefix': '🌿 Hier ist deine Idee:',
        'feedback': ['👍 Hat mir gefallen', '👎 Nicht für mich'],
        'feedback_responses': [
            'Ich bin wirklich glücklich, das zu hören! :)',
            'Keine Sorge! Versuche eine andere Idee.'
        ],
        'language_label': 'Sprache wählen',
        'instructions': [
            '🚀 Wie zu verwenden:',
            'Wähle deine Sprache oben',
            'Fülle die vier Fragen aus',
            'Erhalte deine personalisierte, aufmunternde Idee!'
        ]
    },
    'fr': {
        'name': 'Français',
        'flag': '🇫🇷',
        'ai_name': 'French',
        'title': '🌞 Inspiration quotidienne',
        'subtitle': 'Laissez-moi, avec un peu d\'aide de l\'IA, égayer votre journée',
        'questions': [
            "Quel temps fait-il maintenant?",
            "Où êtes-vous? (Au travail ou à la maison, en ville ou à la campagne?)",
            "Comment vous sentez-vous émotionnellement?",
            "Quelque chose vous préoccupe-t-il aujourd'hui?"
        ],
        'button': 'Obtenir mon idée inspirante 🏄‍♂️',
        'fill_warning': 'Veuillez remplir tous les champs pour obtenir votre idée',
        'thinking': 'Je réfléchis...',
        'idea_prefix': '🌿 Voici votre idée:',
        'feedback': ['👍 J\'ai aimé', '👎 Pas pour moi'],
        'feedback_responses': [
            'Je suis vraiment heureux d\'entendre cela! :)',
            'Pas de souci! Essayez une autre idée.'
        ],
        'language_label': 'Choisir la langue',
        'instructions': [
            '🚀 Comment utiliser:',
            'Choisissez votre langue en haut',
            'Remplissez les quatre questions',
            'Obtenez votre idée inspirante personnalisée!'
        ]
    },
    'fi': {
        'name': 'Suomi',
        'flag': '🇫🇮',
        'ai_name': 'Finnish',
        'title': '🌞 Päivittäinen inspiraatio',
        'subtitle': 'Anna minun, tekoälyn avulla, piristää päivääsi',
        'questions': [
            "Millainen sää on nyt?",
            "Missä olet? (Töissä vai kotona, kaupungissa vai maaseudulla?)",
            "Miten voit henkisesti?",
            "Onko jokin asia huolestuttamassa sinua tänään?"
        ],
        'button': 'Saa inspiroiva ideani 🏄‍♂️',
        'fill_warning': 'Täytä kaikki kentät saadaksesi ideasi',
        'thinking': 'Ajattelen...',
        'idea_prefix': '🌿 Tässä on ideasi:',
        'feedback': ['👍 Pidin siitä', '👎 Ei minulle'],
        'feedback_responses': [
            'Olen todella iloinen kuullessani sen! :)',
            'Ei hätää! Kokeile toista ideaa.'
        ],
        'language_label': 'Valitse kieli',
        'instructions': [
            '🚀 Kuinka käyttää:',
            'Valitse kielesi ylhäältä',
            'Täytä neljä kysymystä',
            'Saa henkilökohtainen inspiroiva ideasi!'
        ]
    }
}

# Streamlit page settings
st.set_page_config(page_title="Daily Uplift", page_icon="🌈")

# Initialize session state
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = 'en'
if 'current_idea' not in st.session_state:
    st.session_state.current_idea = None
if 'show_idea' not in st.session_state:
    st.session_state.show_idea = False
if 'feedback' not in st.session_state:
    st.session_state.feedback = None

# Language selector at the top
# st.markdown("### " + LANGUAGES[st.session_state.selected_language]['language_label'])

cols = st.columns(len(LANGUAGES))
for i, (lang_code, lang_data) in enumerate(LANGUAGES.items()):
    with cols[i]:
        # if st.button(f"{lang_data['flag']} {lang_data['name']}",
        if st.button(f"{lang_data['name']}",
                     key=f"lang_{lang_code}",
                     use_container_width=True,
                     type="secondary" if lang_code == st.session_state.selected_language else "secondary"):
            st.session_state.selected_language = lang_code
            st.session_state.show_idea = False  # Reset when language changes
            st.session_state.feedback = None
            st.rerun()

# Get current language config
lang = LANGUAGES[st.session_state.selected_language]
current_lang_code = st.session_state.selected_language

# Display title and subtitle in selected language
st.title(lang['title'])
st.subheader(lang['subtitle'])

# Get current local time and day
now = datetime.now()
current_time = now.strftime("%H:%M")
current_day = now.strftime("%A")
time_of_day = (
    "morning" if 5 <= now.hour < 11 else
    "afternoon" if 11 <= now.hour < 18 else
    "evening" if 18 <= now.hour < 22 else
    "night"
)

# Prompt templates (in English for the AI)
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

# User input using array indexing for questions
user_inputs = []
for i, question in enumerate(lang['questions']):
    user_input = st.text_input(f"{i + 1}. {question}")
    user_inputs.append(user_input)

weather, location, mood, worry = user_inputs

if st.button(lang['button']):
    if not all(user_inputs):
        st.warning(lang['fill_warning'])
    else:
        with st.spinner(lang['thinking']):
            # Randomly choose a template
            prompt = random.choice(prompt_templates)

            # Determine language instruction for the AI
            language_instruction = "" if current_lang_code == 'en' else f"Respond in {lang['ai_name']}. "

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": (
                            f"You are a warm, kind, emotionally intelligent friend. "
                            f"{language_instruction}"
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
                            f"- Location: {location}\n"
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
    st.success(f"{lang['idea_prefix']}\n\n{st.session_state.current_idea}")

    # Rating buttons using array indexing
    col1, col2 = st.columns(2)


    def give_feedback(rating):
        st.session_state.feedback = rating


    with col1:
        if st.button(lang['feedback'][0]):  # Like button
            give_feedback("liked")

    with col2:
        if st.button(lang['feedback'][1]):  # Dislike button
            give_feedback("disliked")

# Show feedback message if available using array indexing
feedback = st.session_state.get("feedback", None)

if feedback == "liked":
    st.success(lang['feedback_responses'][0])
elif feedback == "disliked":
    st.warning(lang['feedback_responses'][1])

# Instructions footer using array
#st.markdown("---")
#st.markdown(f"### {lang['instructions'][0]}")
#for i in range(1, len(lang['instructions'])):
#    st.markdown(f"{i}. {lang['instructions'][i]}")

# to start run in terminal: streamlit run inspiration_app_lang.py