
import streamlit as st
from streamlit_modal import Modal
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from splitters import *
import sqlite3
import hashlib

#-----------------------------------------------------------------------

st.set_page_config(    
    page_title="Kidney Chat - Process",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
    )

hide_menu_style = """
        <style>
        MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        footer:before {
            content:'Brought to you by: The Road Back To Life'; 
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 5px;
            top: 2px;
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
        .st-emotion-cache-lrlib {
            padding-top: 3rem;
        }    
        .st-emotion-cache-17lntkn {
            color: black;
        }         
        .st-emotion-cache-1y4p8pa {
            width: 100%;
            padding: 2rem 1rem 10rem;
            max-width: 95%
        }
        .st-emotion-cache-1oe5cao {
            padding-top: 3rem;
        }
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)  

#-----------------------------------------------------------------------

if 'loggedin' not in st.session_state:
    st.session_state['loggedin'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = ''

#-------------------------------------------------------
    
def embed_index(doc_list, embed_fn, index_store):
  """Function takes in existing vector_store, 
  new doc_list and embedding function that is 
  initialized on appropriate model. Local or online. 
  New embedding is merged with the existing index. If no 
  index given a new one is created"""

  #check whether the doc_list is documents, or text
  try:
      faiss_db = FAISS.from_documents(doc_list, embed_fn) 
  except Exception as e:
      faiss_db = FAISS.from_texts(doc_list, embed_fn)

  if os.path.exists(index_store):
    local_db = FAISS.load_local(index_store, embed_fn)
    #merging the new embedding with the existing index store
    local_db.merge_from(faiss_db)
    local_db.save_local(index_store)
  else:
    faiss_db.save_local(folder_path=index_store)
 
#-------------------------------------------------------
    
directory = 'docs'
    
def save_file(uploaded_file):
   with open(os.path.join(directory, uploaded_file.name), "wb") as f:
      f.write(uploaded_file.getbuffer())

#-------------------------------------------------------

# Initialize the database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL)''')
conn.commit()

#-------------------------------------------------------

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def signin(username, password):
    """Sign in a user and handle signin logic."""
    password_hash = hash_password(password)
    c.execute("SELECT * FROM users WHERE username=? AND password_hash=?", (username, password_hash))
    user = c.fetchone()
    conn.close()
    return user is not None

#-------------------------------------------------------

def show_process():
    if st.session_state['loggedin'] == True:

        tab1, tab2 = st.tabs(["Upload Documents", "View Summaries"])

        with tab1:
            st.header("Upload Documents")

            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            index_store = 'db'
            source_files = []

            files = st.file_uploader(label="To import 'pdf', 'txt', 'csv' documents into the library:", type=['pdf', 'txt', 'csv'], accept_multiple_files=True)

            if st.button("Process"):
                st.markdown('---')
                with st.spinner("Processing..."):
                    if files is not None:
                        for file in files:
                            # st.write(file.name)
                            save_file(file)
                            source_files.append(os.path.join(directory, file.name))

                        for source_file in source_files:
                            st.write('Processing: ' + source_file)
                            if source_file.endswith('.txt'):
                                docs = get_text_splits(source_file)
                            elif source_file.endswith('.pdf'):
                                docs = get_pdf_splits(source_file)
                            elif source_file.endswith('.csv'):
                                docs = get_csv_splits(source_file)

                            embed_index(doc_list=docs,
                                embed_fn=embeddings,
                                index_store=index_store) 
                            
                st.success(' Success!', icon="✅")
        with tab2:
            st.header("Summaries")
            conn = sqlite3.connect('utils.db')
            c = conn.cursor()
            c.execute('''SELECT * FROM survey ORDER BY date_stamp DESC''')
            rows = c.fetchall()
            for row in rows:
                st.write("Date: " + row[0] + "  -  Satisfied: " + str(row[1]) + "  \nComment: " + row[2])

                print(row[0] + " - " + str(row[1]) + " - " + row[2])

#-------------------------------------------------------

def show_signin():
    if st.session_state['loggedin'] == False:
        st.write("You must sign in to access this area...")
        form = st.form("signin_form")
        with form:
            login_username = st.text_input('Username')
            login_password = st.text_input('Password', type="password")
            login_button = st.form_submit_button('Sign In')
            if login_button:
                if not signin(login_username, login_password):
                    st.error('Login failed. Incorrect username or password.')
                else:
                    st.success('Login successful!')
                    st.session_state['loggedin'] = True
                    st.rerun()

#-------------------------------------------------------
                    
def main():                  
    show_signin()       
    show_process() 

if __name__ == "__main__":
    main()

#-------------------------------------------------------