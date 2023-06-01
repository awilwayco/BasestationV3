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

@st.cache(allow_output_mutation=True)
def read_button_state():
    with open("database.txt", "r") as file:
        return file.read() == "True"

@st.cache(allow_output_mutation=True)
def write_button_state(button_state):
    with open("database.txt", "w") as file:
        file.write(str(button_state))

button_state = read_button_state()

if st.button("True/False Button", key="button"):
    button_state = not button_state
    write_button_state(button_state)

if button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
