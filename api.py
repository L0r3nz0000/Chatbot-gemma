import keras_nlp
from ChatState import ChatState, display_chat
import markdown

from flask import Flask, render_template, request, redirect

gemma_lm = keras_nlp.models.CausalLM.from_preset("Gemma1-2b")
gemma_lm.compile(sampler="greedy")
#gemma_lm.compile(sampler="top_k")  # Creative mode

chat = ChatState(gemma_lm)

app = Flask(__name__)

# @app.route("/get_chat")
# def chat():
#     return chat.get_json()

@app.route("/send_prompt", methods=['POST'])
def send_prompt():
    message = request.form.get('prompt')
    if message != None:
        answer = chat.send_message(message)
    else:
        return "<h1>Errore nella richiesta a /send_prompt</h1>"
    
    return redirect("/")

@app.route("/", methods=['GET'])
def index():
    chat_json = chat.get_history_as_json()
    messages = ""
    
    for message in chat_json:
        messages += f"<div class=\"message message-right\">{markdown.markdown(message['user'])}</div>" # USER PROMPT
        messages += f"<div class=\"message message-left\">{markdown.markdown(message['model'])}</div>" # MODEL OUTPUT
    
    return render_template('index.html', messages=messages)