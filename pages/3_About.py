import streamlit as st

hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
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
            .st-emotion-cache-lrlib {
                padding-top: 3rem;
            }    
            .st-emotion-cache-17lntkn {
                color: black;
            }
            </style>
            """
        
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.write("About page")