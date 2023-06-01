import streamlit as st
import requests
import base64

def write_to_github(file_path, repository_owner, repository_name, branch_name, content, access_token):
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_path}"
    headers = {"Authorization": f"Bearer {access_token}"}

    # Retrieve the current file content
    response = requests.get(url, headers=headers)
    response_json = response.json()
    if response.status_code == 200:
        file_data = response_json["content"]
        file_sha = response_json["sha"]

        # Prepare the new content
        content_bytes = content.encode("utf-8")
        content_base64 = base64.b64encode(content_bytes).decode("utf-8")

        # Update the file with the new content
        data = {
            "message": "Updated file",
            "content": content_base64,
            "sha": file_sha,
            "branch": branch_name
        }

        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 200:
            print("File updated successfully")
        else:
            print(f"Error updating file: {response.text}")
    else:
        print(f"Error retrieving file: {response.text}")

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
      
file_path = "database.txt"
repository_owner = "awilwayco"
repository_name = "BasestationV3"
branch_name = "main"
access_token = "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"

button_state = read_button_state()

if st.button("True/False Button", key="button"):
    button_state = not button_state
    content = str(button_state)
    write_to_github(file_path, repository_owner, repository_name, branch_name, content, access_token)

if button_state:
    st.write("Button is True")
else:
    st.write("Button is False")
