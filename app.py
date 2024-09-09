import os
import sqlite3
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


if not openai_api_key:
    raise ValueError("OpenAI API Key not found in environment variables.")


os.environ["OPENAI_API_KEY"] = openai_api_key

llm = ChatOpenAI(model="gpt-4")

def gpt_generate_questions(user_input):
    prompt_template = """
    Based on the following medical scenario, generate 4 follow-up questions that are relevant to the symptoms mentioned:
    
    Scenario: "{input}"
    
    Questions:
    """
    prompt = PromptTemplate(
        input_variables=["input"],
        template=prompt_template
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.run({"input": user_input})
    return response.strip().split("\n")

# Set up a database connection
conn = sqlite3.connect('medical_data.db')
cursor = conn.cursor()

# Create a table to store the conversations with an additional column for initial symptoms
cursor.execute('''
CREATE TABLE IF NOT EXISTS MedicalConversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    initial_symptoms TEXT,
    follow_up_question_1 TEXT,
    answer_1 TEXT,
    follow_up_question_2 TEXT,
    answer_2 TEXT,
    follow_up_question_3 TEXT,
    answer_3 TEXT,
    follow_up_question_4 TEXT,
    answer_4 TEXT
)
''')

def medical_chatbot():
    initial_symptoms = input("Please describe your medical symptoms: ")
    follow_up_questions = gpt_generate_questions(initial_symptoms)

    answers = []
    for i, question in enumerate(follow_up_questions, start=1):
        if i > 4:
            break  # We only handle up to 4 questions
        print(question)
        answer = input("Your response: ")
        answers.append((question, answer))

    # Prepare data to match the table structure, filling in None for missing values
    data_to_insert = (initial_symptoms, ) + tuple([item for sublist in answers for item in sublist] + [None] * (8 - len(answers) * 2))
    
    cursor.execute('''
    INSERT INTO MedicalConversations (initial_symptoms, follow_up_question_1, answer_1, follow_up_question_2, answer_2, follow_up_question_3, answer_3, follow_up_question_4, answer_4)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_to_insert)

    conn.commit()
    print("\nData has been saved successfully!")

medical_chatbot()
