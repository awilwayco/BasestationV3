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

# Read the current button state from the file
with open("button_state.txt", "r") as file:
    button_state = file.read() == "True"

# Create a button and update the file with the new state when clicked
if st.button("True/False Button", key="button"):
    button_state = not button_state
    with open("button_state.txt", "w") as file:
        file.write(str(button_state))

# Display the boolean value based on the button state
if button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
