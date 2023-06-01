import streamlit as st
import requests

def write_to_github(file_path, repository_owner, repository_name, branch_name, content, access_token):
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_path}"
    headers = {"Authorization": f"Bearer {access_token}"}

    data = {
        "message": "Updated file",
        "content": content,
        "branch": branch_name
    }

    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        st.success("File updated successfully")
    else:
        st.error(f"Error updating file: {response.text}")

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
      
file_path = st.text_input("database.txt")
repository_owner = st.text_input("awilwayco")
repository_name = st.text_input("BasestationV3")
branch_name = st.text_input("main")
content = st.text_area(str(button_state))
access_token = st.text_input("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")

button_state = read_button_state()

if st.button("True/False Button", key="button"):
    button_state = not button_state
    write_to_github(file_path, repository_owner, repository_name, branch_name, content, access_token)

if button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
