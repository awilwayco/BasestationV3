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

i1 = st.button("button 1")
st.write("value:", i1)
