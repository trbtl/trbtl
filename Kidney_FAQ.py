
# python -m venv venv
# venv\Scripts\activate
# pip install -r requirements.txt
# streamlit run Kidney_FAQ.py

import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain 
from apikey_hungingface import apikey_hungingface
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
import os

st.set_page_config(
    page_title="Kidney FAQ",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
    ) 

# Set Hugging Face Hub API token
# Make sure to store your API token in the `apikey_hungingface.py` file
os.environ["HUGGINGFACEHUB_API_TOKEN"] = apikey_hungingface
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["apikey_hungingface"]
# st.write(st.secrets["apikey_hungingface"])
# st.write(os.environ["HUGGINGFACEHUB_API_TOKEN"] )
target_source_chunks = 6
index_store = 'db'

# Initialise session state variables
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

#-----------------------------------------------------

custom_template = """
This is conversation with a human at grade level 8. Answer the questions you get based on the knowledge you have.
If you don't know the answer, just say that you don't, don't try to make up an answer.
Chat History:
{chat_history}
Follow Up Input: {question}
"""
CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local(index_store, embeddings)
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": target_source_chunks})
memory = ConversationBufferMemory(memory_key="chat_history", input_key='question', output_key='answer',return_messages=True)
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.01, "max_new_tokens": 500})

qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever,
    condense_question_prompt=CUSTOM_QUESTION_PROMPT,
    memory=memory,
    return_source_documents=True
)

#-----------------------------------------------------

# Create the Streamlit app
def main():  
    st.subheader('Kidney FAQ 💬')
 
    # Sidebar contents
    with st.sidebar:
        st.title('Kidney FAQ 💬')           
        st.markdown('''
Kidney FAQ is brought to you by:\n 
[The Road Back To Life](https://kidneysupportgroup.org/)
                    ''')

    hide_menu_style = """
            <style>
            #MainMenu {
                visibility: hidden;
                }
            header {
                visibility: hidden;
                height: 0%;
                }
            div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
            div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
            div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
            footer {
                visibility: hidden;
                }
            footer:after {
                content:'Brought to you by: The Road Back To Life'; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 5px;
                bottom: 2px;
            } 
            [data-testid="stToolbar"] {visibility: hidden !important;}
            .st-emotion-cache-1oe5cao {
                padding-top: 3rem;
            } 
            #GithubIcon {
                visibility: hidden;
            }
            .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
            .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
            .viewerBadge_text__1JaDK {
                display: none;
            }    
            .st-emotion-cache-17lntkn {
                color: black;
            }
            .css-1y4p8pa  {
                padding: 2rem 1rem 5rem;
            }
            .st-emotion-cache-1ru4d5d {
                padding: 2rem 1rem 1rem;
            }
            .css-90vs21 {
                padding-bottom: 30px;
            }
            .st-emotion-cache-1ru4d5d {
                max-width: 90%;
            }
            .st-emotion-cache-139wi93 {
                max-width: 90%;
                padding: 1.5rem 1rem 1.5rem
            }
            .st-emotion-cache-uhkwx6 {
                background-color: lightgrey;
                border: solid grey;
                border-radius: 10px;
            }
            .st-emotion-cache-lrlib {
                padding-top: 3rem;
            }            
            .st-emotion-cache-mcjgwn {
                padding-top: 3rem;
             }          
            .st-emotion-cache-1wm93xv {
                padding: 1rem 1.5rem 1rem; 
            }               
            </style>
            """
        
    st.markdown(hide_menu_style, unsafe_allow_html=True)

#-----------------------------------------------------    

    acontainer = st.container()
    clear_button = st.sidebar.button("New Conversation", key="clear")

    # reset everything
    if clear_button:
        st.session_state['history'] = []
        st.session_state['generated'] = []
        st.session_state['past'] = []

    # Get user input
    question = st.chat_input("Ask a question:")

    with st.spinner("Generating Answer..."):
        if question:
            response = qa({"question": question})
            # print(response['answer'])
            # print('')
            # print('----------------------------------------------------')
            # print('')

            st.session_state['past'].append("❓ Question: " + question)
            st.session_state['generated'].append("✨ Answer: " + response['answer'])
            st.session_state['history'].append("Question: " + question) 
            st.session_state['history'].append(response['answer'])      
            
    if st.session_state['generated']:
        with acontainer:
            for i in range(len(st.session_state['generated'])):
                acontainer.write(st.session_state["past"][i])
                acontainer.write(st.session_state["generated"][i])

if __name__ == "__main__":
    main()