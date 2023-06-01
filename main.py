import streamlit as st

# Hide Streamlit Style
hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        </style>
                        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Title
st.markdown("<h1 style='text-align: center; color: white;'>SWAMP Blimps</h1>", unsafe_allow_html=True)

if 'button_state' not in st.session_state:
    st.session_state.button_state = False

if st.button("True/False Button"):
    st.session_state.button_state = not st.session_state.button_state

if st.session_state.button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
