import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get("OPENAI_KEY")
completion = openai.Completion()

start_chat_log = '''Humans: Hello, who are you?\n AIs: I am doing great. How can I help you today?'''

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
        print(f"before chatlog none, after:{chat_log}")
        # to continue the chat and if there any we star withe the message
    # give a format with the answer to the AI
    prompt = f'{chat_log}Human: \n{question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'

