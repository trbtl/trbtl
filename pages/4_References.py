# venv\Scripts\activate

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
# import base64
import os

#-----------------------------------------------------------------------

st.set_page_config(    
    page_title="Kidney Chat - References",
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

# Initialize the selected_file in session state if it's not already present
if 'selected_file' not in st.session_state:
    st.session_state['selected_file'] = None

def get_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

#-----------------------------------------------------------------------

def main(): 
    with st.sidebar:
        library = st.container()
        with library:
            def get_files(directory):
                return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

            def file_selector(folder_path='.'):
                st.write("Select a document to view from the list below:")
                files = get_files(folder_path)
                for file in files:
                    if st.button(file): 
                        st.session_state['selected_file'] = file  

            folder_path = './docs' 
            file_selector(folder_path)

#-----------------------------------------------------------------------
       
    if st.session_state['selected_file'] is not None: 
        with st.spinner("Processing..."):       
            filename = st.session_state['selected_file']
            # st.write(filename)
            folder_path = './docs'  
            uploaded = os.path.join(folder_path, filename)
        
            pdf_viewer(input=uploaded, width=1000)
            # pdf_viewer(input=uploaded, width=1000)
#-----------------------------------------------------------------------
 
if __name__ == "__main__":
    main()