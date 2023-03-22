import streamlit as st
from streamlit_chat import message as st_message


import random

import openai

# set up the OpenAI API key
openai.api_key = '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'

# set up the OpenAI model ID
model_id = 'text-davinci-003'



# define a function to interact with ChatGPT
def chat_with_gpt(message):
    # generate a response message using the OpenAI API
    response = openai.Completion.create(
        engine=model_id,
        prompt=f'You: {message}\nChatGPT:',
        max_tokens=200
    ).choices[0].text.strip()
    # print the response message
    return f'suriya: {response}'

# start a loop to interact with ChatGPT






responses = {
"hi": "Hi baby!",
"saptiya":["illa baby ni saptiya","saptan baby ni saptiya"],
"enna panra":["summa thaan baby ni","onna thaan d think"],
"call pannu":"panran",
"enna da pannra":["summa thaan baby ni","onna thaan d think"],
"padika poran":"padi baby",
"mm":"mm",
"vitu":"sari",
"hloo": "Hello pondati",
"hello": "Hello baby",
"how are you": "I'm great, how about you?",
"what are you up to": "Just thinking about you :)",
"tell me about yourself": "I'm Suriya, your loving partner who created this chatbot just for you.",
"what do you like": "I like spending time with you.",
"what are your hobbies": "My hobbies include programming and spending time with you.",
"do you love me": "Of course I love you more than anything!",
"what is your favorite food": "My favorite food is anything that you cook for me.",
"what is your favorite movie": "My favorite movie is the one we watched together last week.",
"what is your favorite song": "My favorite song is the one that reminds me of you.",
"good morning": "Good morning my love, I hope you slept well.",
"good night baby": "Good night Abinaya, sweet dreams!",
"miss you": "I miss you so much my love, can't wait to see you again.",
"love you": "I love you more than anything Abinaya!",
"bye": "Bye for now, talk to you soon!",
"take care": "You too Abinaya, take care of yourself.",
"suriya":["sulu","baby"],
"eruma":"bannu",
"good night":"lovly kissy rommantic night",
"no":"pee",
"loosu":"oun malathaan d",
"sry":"vidu",
"enna":["va valangani povum","kiss pannu","onna vachi saivan","saptiya"],
"dei":["yanna d","ayi"],
"periods baby":"next time varama pathukuran baby",
"periods":"konjam porukutha baby adutha 10 month ku varama pathukuran",
"poriki":"oun pinadi thaan d"
}

def generate_response(user_input):
    user_input=str.lower(user_input)
    print(user_input)
    response = responses.get(user_input.lower())
    print(type(response))
    
    if response:
        if isinstance(response, list):
            return random.choice(response)
        else:
            return "suriya: {}".format(response)
    else:
        
        return chat_with_gpt(user_input)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("baby")

listx=[]
listy=[]
def generate_answer():
    
    user_message = st.session_state.input_text
    message_bot =generate_response(user_message)
    while True:
        x=random.randint(0, 1000000)
        if x in listx:
            continue
        else:
            listx.append(x)
            break
    while True:
        y=random.randint(1000000,100000000)
        if y in listy:
            continue
        else:
            listy.append(y)
            break
        

    st.session_state.history.append({"message": user_message, "is_user": True,'key': 'chat{}'.format(x)})
    st.session_state.history.append({"message": message_bot, "is_user": False,'key': 'chat{}'.format(y)})




for chat in st.session_state.history:
    st_message(**chat)  # unpacking
    
st.text_input("Talk to baby", key="input_text", on_change=generate_answer)