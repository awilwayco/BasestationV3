#!/usr/bin/env python3
import streamlit as st
import os
from git import Repo

cmd = 'pip install GitPython'
os.system(cmd)

def write_to_github(file_path, repository_url, branch_name, content):
    # Clone the repository
    repo = Repo.clone_from(repository_url, "temp_folder")
    
    # Checkout the branch
    repo.git.checkout(branch_name)
    
    # Modify the file content
    file_path_in_repo = f"temp_folder/{file_path}"
    with open(file_path_in_repo, "w") as file:
        file.write(content)
    
    # Commit and push the changes
    repo.git.add(file_path_in_repo)
    repo.index.commit("Updated file")
    repo.git.push("origin", branch_name)

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

file_path = "database.txt"
repository_url = "https://github.com/your-username/your-repo.git"
branch_name = "main"

@st.cache(allow_output_mutation=True)
def read_button_state():
    with open(file_path, "r") as file:
        return file.read() == "True"
     
repository_owner = "awilwayco"
repository_name = "BasestationV3"
branch_name = "main"
access_token = "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"

button_state = read_button_state()

if st.button("True/False Button", key="button"):
    button_state = not button_state
    content = str(button_state)
    write_to_github(file_path, repository_url, branch_name, content)
    #write_to_github(file_path, repository_owner, repository_name, branch_name, content, access_token)

if button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
