
import streamlit as st

#-----------------------------------------------------------------------

st.set_page_config(    
    page_title="Kidney Chat - About",
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
        .st-emotion-cache-1oe5cao {
            padding-top: 3rem;
        }
        .st-emotion-cache-lrlib {
            padding-top: 3rem;
        } 
        </style>
        """
    
st.markdown(hide_menu_style, unsafe_allow_html=True)

def main(): 
    tab1, tab2, tab3, tab4 = st.tabs(["About", "Who is The Road Back To Life?", "Survey", "History"])

    with tab1:
        st.header("Welcome to Kidney Chat")
        st.markdown("""
    The Kidney Chat application was created to help you with your questions about kidney disease and related topics. 
    Kidney Chat is trained on a collection of documents concerning kidney disease exclusively, so you can be confident of the source of the answers. If you click on “References” in the sidebar on left side of the screen you will be taken to a page where you can see a list of those documents and be able to review them if you wish.
    """)

    with tab2:
        st.header("Who is The Road Back To Life?")
        st.markdown("""    
        The Road Back To Life is an organization dedicated to providing hope, education, and mentorship to individuals affected by kidney disease. They believe that a diagnosis of kidney disease does not mean the end of life, and with advancements in treatments, many patients can lead fulfilling lives. Their mission is to offer support to all individuals, including patients, partners, and friends, as they navigate this new chapter. They understand the emotional and physical toll of kidney disease and strive to empower and educate those affected, while providing a sense of community and understanding during this difficult time.
        """)

    with tab3:
        st.header("Survey")
        st.text(
        "Would you be willing to share your satisfaction level with Kidney Chat?\nEverything here is totally anonymous.")

        satisfaction = st.radio(
            "Satisfaction level:",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            index=None, horizontal=True
            )
        # st.write("You selected:", satisfaction)

        comment = st.text_area("Comments:", placeholder="Enter your comments")

        if st.button("Submit your comments here."):
            st.write(satisfaction, comment)
    with tab4:
        st.header("History")
        st.markdown("""
        This is Version 0.01 \n
        Concept: \n
        The difference between Kidney Chat and other AI tools, such as ChatGPT, is that it is focused on kidney disease exclusively.  ChatGPT and other general purpose AI tools are more general in nature and try to be everything to everybody.   Kidney Chat does have some general knowledge. You can ask it some basic questions, but it doesn’t attempt to compete with other types of AI tools, so you may be disappointed with the results.   ChatGPT is trained (they claim) on the whole internet so its knowledge base is vast, but how can be sure of where its answers are generated from.  
        """)

if __name__ == "__main__":
    main()




# Satisfaction level: <br>
# 1   2   3   4    5   6   7   8   9   10 <br>
# Brief comments: <br>
# [_______________________________________________]