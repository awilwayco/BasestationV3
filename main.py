import streamlit as st
import sys

# Add the path to the pygithub package
sys.path.append('/home/appuser/venv/lib/python3.9/site-packages')
from github import Github

access_token = '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'
g = Github(access_token)

def write_to_github(file_path, repository_name, branch_name, content):
    repo = g.get_user().get_repo(repository_name)
    branch = repo.get_branch(branch_name)
    file = repo.get_contents(file_path, ref=branch.name)
    repo.update_file(file.path, "Commit message", content, file.sha, branch=branch.name)

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

file_path = 'database.txt'
repository_name = 'BasestationV3'
branch_name = 'main'  # or the name of the branch where the file is located
content = str(button_state)

write_to_github(file_path, repository_name, branch_name, content)

button_state = read_button_state()

if st.button("True/False Button", key="button"):
    button_state = not button_state
    write_button_state(button_state)

if button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
