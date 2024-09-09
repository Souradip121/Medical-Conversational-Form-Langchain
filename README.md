# Medical Conversational Form

This project is a medical chatbot that uses OpenAI's GPT-4 model to generate follow-up questions based on user input about their medical symptoms. The chatbot interacts with the user, asks 4 follow-up questions, and stores the conversation, including initial symptoms and responses, in a SQLite database.

## Features

- Uses OpenAI's GPT-4 model to generate medically relevant follow-up questions.
- Stores the initial symptoms, generated questions, and user responses in an SQLite database.
- User inputs are saved locally in a SQLite database (`medical_data.db`).
- Environment variables are used to securely manage the OpenAI API key.

## Prerequisites

- Python 3.8 or later
- An OpenAI API key (You can get one by signing up for [OpenAI](https://platform.openai.com/)).

## Setup Instructions

### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/Medical-Conversational-Form.git
cd Medical-Conversational-Form
```

### 2. Create and activate a virtual environment

It's recommended to create a virtual environment to manage dependencies. You can do this as follows:

#### On Windows:

```bash
python -m venv my_env
my_env\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv my_env
source my_env/bin/activate
```

### 3. Install dependencies

Once your virtual environment is activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following packages:

- `langchain` - for interacting with OpenAI's GPT-4 model.
- `openai` - OpenAI's official Python library.
- `python-dotenv` - for managing environment variables.


### 4. Set up your environment variables

To securely manage your OpenAI API key, create a `.env` file in the root directory of the project. Inside `.env`, add the following line:

```
OPENAI_API_KEY=sk-your-api-key-here
```

Replace `sk-your-api-key-here` with your actual OpenAI API key.

### 5. Add `.env` and `my_env` to `.gitignore`

Ensure that your `.env` file is not accidentally pushed to version control. The `.gitignore` file should already contain the following line, but verify it is present:

```plaintext
.env
my_env\

```

### 6. Run the chatbot

Once everything is set up, run the chatbot by executing:

```bash
python app.py
```

### How the Chatbot Works:

1. The user is prompted to describe their medical symptoms.
2. GPT-4 generates 4 follow-up questions based on the symptoms provided.
3. The user answers each question, and the chatbot stores the conversation (initial symptoms, questions, and answers) in a local SQLite database (`medical_data.db`).
4. The chatbot confirms when the data has been saved successfully.

### 7. Viewing the Data

The conversations are saved in an SQLite database named `medical_data.db`. You can explore or query the database using SQLite tools like `sqlite3` in Python, or external tools such as [DB Browser for SQLite](https://sqlitebrowser.org/).

Example query to view all stored conversations:

```sql
SELECT * FROM MedicalConversations;
```

### Database Schema

The `MedicalConversations` table has the following columns:

- `id`: Unique identifier (auto-incremented).
- `initial_symptoms`: User's initial symptom description.
- `follow_up_question_1`: The first generated follow-up question.
- `answer_1`: User's response to the first follow-up question.
- `follow_up_question_2`: The second generated follow-up question.
- `answer_2`: User's response to the second follow-up question.
- `follow_up_question_3`: The third generated follow-up question.
- `answer_3`: User's response to the third follow-up question.
- `follow_up_question_4`: The fourth generated follow-up question.
- `answer_4`: User's response to the fourth follow-up question.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Feel free to contribute by submitting issues or pull requests to improve the chatbot.

## Contact

For any questions or issues, feel free to open an issue on the repository or contact the project maintainer.
