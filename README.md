
DAILY UPLIFT APP
================

Overview
--------
Daily Uplift is an interactive app that delivers personalized, emotionally intelligent ideas to uplift your mood. Using OpenAI's GPT-3.5 model and built with Streamlit, the app helps you reflect on your emotions, environment, and thoughts—and responds with short, imaginative suggestions to brighten your day.

Two Versions Available
----------------------
1. **English Version**:
   - A straightforward interface with all interactions in English.
   - Best for quick use or initial setup.

2. **Multilingual Version**:
   - Offers full support for English 🇺🇸, Russian 🇷🇺, German 🇩🇪, French 🇫🇷, and Finnish 🇫🇮.
   - Includes localized interface, prompts, and AI-generated responses.
   - Dynamic language selection and culturally adapted messages.

Features
--------
- Personalized ideas based on weather, location, mood, and current worries
- Optimized prompt generation tailored to the time of day
- Feedback mechanism (Like/Dislike) with contextual response
- Streamlit-powered web UI
- Quick setup and smooth local execution

Prerequisites
-------------
- Python 3.7 or higher
- Streamlit
- OpenAI API Key

Setup Instructions
------------------

1. Clone the repository:
    git clone https://github.com/yourusername/daily-uplift.git
    cd daily-uplift

2. Create and activate a virtual environment:
    - Windows:
        python -m venv .venv
        .\.venv\Scripts\activate
    - macOS/Linux:
        python3 -m venv .venv
        source .venv/bin/activate

3. Install dependencies:
    pip install -r requirements.txt

4. Set your OpenAI API key:
    - Windows:
        set OPENAI_API_KEY=your_api_key_here
    - macOS/Linux:
        export OPENAI_API_KEY=your_api_key_here

    Optional: Create a .env file with:
        OPENAI_API_KEY=your_api_key_here

5. Run the app:
    - For English version:
        streamlit run inspiration_app.py
    - For Multilingual version:
        streamlit run inspiration_app_lang.py

Usage
-----
1. Choose version based on your preference (English or multilingual).
2. Answer four quick questions about your situation.
3. Receive a customized idea to lift your spirits.
4. Optionally give feedback on the suggestion.

Languages (Multilingual Version)
--------------------------------
- English 🇺🇸
- Russian 🇷🇺
- German 🇩🇪
- French 🇫🇷
- Finnish 🇫🇮

Contributing
------------
We welcome community contributions. Fork the repository, implement your feature or fix, and submit a pull request.

License
-------
MIT License

Acknowledgements
----------------
- OpenAI for GPT-3.5
- Streamlit for the application framework
- Everyone who contributed or tested

Contact
-------
For questions or feedback, open an issue or email: juls.petersburg@gmail.com

Enjoy Your Daily Uplift! 🌞✨
