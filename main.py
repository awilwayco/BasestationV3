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

def get_session_state():
    session_state = SessionState.get(button_state=False)
    return session_state

session_state = get_session_state()

if st.button("True/False Button"):
    session_state.button_state = not session_state.button_state

if session_state.button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
