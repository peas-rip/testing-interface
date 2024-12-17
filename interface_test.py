import streamlit as st
from chatbot import chatres
import os
#html section 

# html_code = """
# <div>
# <p>Hello World</p>
# </div>
# """
#st.markdown(html_code, unsafe_allow_html=True)
interface=st.html("<h1>Team A Interface</h1>")

with st.container():

    text=st.chat_input("Help?")
    if text:
        #use required agents response function 

        randorm_text=chatres()

        #string to generate an agents response


        st.write(randorm_text)
    else:
        #warning if no text input

        st.warning("Please enter a text")

with st.container():
    uploaded_file = st.file_uploader("Choose a file", type="docx")
    # if uploaded_file is not None:
    #     # if not os.path.exists('D:\Sprint\team_a_interface\uploaded_files'):
    #     #     os.makedirs('D:\Sprint\team_a_interface\uploaded_files')
    #     # file_path='D:\Sprint\team_a_interface\uploaded_files'
    #     # with open(file_path, "wb") as f:
    #     #     f.write(uploaded_file.getbuffer())
    #     #     bytes_data = uploaded_file.read()
    #     #     st.write("filename:", uploaded_file.name)
    #     #     st.write(bytes_data)
    #     #     # st.success(f"File '{uploaded_file.name}' uploaded successfully and saved to '{file_path}'")
    #     if not os.path.exists(r"D:\Sprint\team_a_interface\uploads"):
    #         os.makedirs(r"D:\Sprint\team_a_interface\uploads")
    #     file_path='D:\Sprint\team_a_interface'
    #     file_path = os.path.join(file_path, uploaded_file.name)
    #     with open(file_path, "wb") as f:
    #         f.write(uploaded_file.getbuffer())
    #         st.success(f"File '{uploaded_file.name}' uploaded successfully and saved to '{file_path}'")

