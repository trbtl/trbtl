
import streamlit as st

#-----------------------------------------------------------------------

st.set_page_config(
    page_title="Kidney FAQ - Instructions",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
    )  

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
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

        .st-emotion-cache-1y4p8pa {
            padding: 3rem 1rem 10rem;
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
        </style>
        """
    
st.markdown(hide_menu_style, unsafe_allow_html=True)

#-----------------------------------------------------------------------

st.title('Instructions')

st.markdown("""
<p>
<h4>Kidney FAQ: </h4>
Type in your kidney related question in the chat box at the bottom of the page. Kidney FAQ will generate an answer based on the documents it has been trained on. <br><br>Kidney FAQ will remember what you’ve been chatting about, so you don’t have to start each new question as if it were the first time.  Think of it as you’re having a conversation with the Kidney FAQ app. <br><br>To begin a new conversation, please click on the “New Conversation” button in the sidebar on the left side of the page.  It will clear out the current conversation you're having, start a new conversation, and won’t remember anything from the previous conversation.
<h4>Instructions: </h4>This Page. <br>
<h4>References: </h4>
Here you will find, listed in the sidebar on the left side of the page, the documents utilized to train Kidney FAQ.  Click on the name of a document and the contents will be displayed in the body of the page. <br>
<h4>Process: </h4>
This is a restricted part of Kidney FAQ, available only to the administrators of the app. <br>
</p>
""",  unsafe_allow_html=True)

#-----------------------------------------------------------------------