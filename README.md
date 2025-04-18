
# Daily Uplift App

## Project Overview

**Daily Uplift** is an interactive app designed to offer personalized uplifting and motivating ideas based on your mood, environment, and worries. Powered by OpenAI’s GPT-3.5 model, this tool generates short, inspiring actions or ideas that help you feel better and more positive.

## Features

- **Personalized Inspiration**: Enter your mood, environment, and worries, and get a tailored uplifting idea.
- **Interactive UI**: A simple, friendly interface built with Streamlit to make it easy to engage with.
- **Flexible**: You can use it daily or whenever you need an inspiring boost.
- **Easy Setup**: Set up quickly and run locally on your machine.

## Prerequisites

Before running the app locally, make sure you have the following:

- **Python 3.7 or higher**
- **Streamlit**
- **OpenAI API Key**

## Setup Instructions

### 1. Clone the repository

To clone the repository to your machine, use the following commands:
```bash
git clone https://github.com/yourusername/daily-uplift.git
cd daily-uplift
```

### 2. Set up a virtual environment

Use a virtual environment to manage dependencies:
- **For Windows**:
  ```bash
  python -m venv .venv
  .\.venv\Scripts ctivate
  ```
- **For macOS/Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install dependencies

Once the environment is set up, install the required libraries using:
```bash
pip install -r requirements.txt
```

### 4. Set up OpenAI API key

You need to obtain an OpenAI API key from [OpenAI's website](https://beta.openai.com/signup/). After obtaining your API key:

- **For Windows**:
  ```bash
  set OPENAI_API_KEY=your_api_key_here
  ```

- **For macOS/Linux**:
  ```bash
  export OPENAI_API_KEY=your_api_key_here
  ```

Alternatively, you can add it to a `.env` file in the root of your project:
```
OPENAI_API_KEY=your_api_key_here
```

If using `.env` files, you’ll need the `python-dotenv` package:
```bash
pip install python-dotenv
```

### 5. Run the app

Now that everything is set up, run the app using:
```bash
streamlit run inspiration_app.py
```

This will launch the app in your default browser.

## How to Use

1. **Answer the prompts**: You’ll be asked to provide the following inputs:
   - **Weather**: How’s the weather right now?
   - **Location**: Where are you? (City, country side, etc.)
   - **Mood**: How are you feeling emotionally today?
   - **Worries**: Is there anything bothering you today?

2. **Get your idea**: After clicking the "✨ Get My Inspiring Idea" button, the app will generate a personalized idea to uplift your mood.

## Contributing

Contributions are welcome! If you have any improvements, bug fixes, or new features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License

## Acknowledgements

- **OpenAI**: For providing the GPT-3.5 API that powers the idea generation.
- **Streamlit**: For creating an easy-to-use framework to build interactive apps.
- **All Contributors**: For helping make this project better!

## Contact Information

For any questions or feedback, please feel free to open an issue in the repository, or contact me via juls.petersburg@gmail.com.

## Enjoy Your Daily Uplift! 🌞✨
