import streamlit as st
from web3 import Web3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
import json

# #load the model
# import tensorflow as tf
# from PIL import Image
# import mouse

load_dotenv()
# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
#w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

################################################################################
# Load model:
################################################################################

import tensorflow as tf
import cv2
file_path=Path('image_model.h5')
model_load=tf.keras.models.load_model(file_path)

#Upload image
img_arr_all=[]
img_arr=cv2.imread('pexels-photo-8416926.jpeg')
if img_arr is not None:
    img_arr=cv2.resize(img_arr,(224,224))
img_arr_all.append(img_arr)
image_resized=tf.image.convert_image_dtype(img_arr_all, dtype='float32')/255.0
model_result=model_load.predict(image_resized)
model_result=int(model_result[:,1])
################################################################################
# Contract Helper function:
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('abi.json')) as f:
        abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=abi
    )

    return contract

contract = load_contract()

################################################################################
# Send money after cleaning kitchen
################################################################################
st.title("Chore - completion")
accounts = w3.eth.accounts
# Use a streamlit component to get the address of the artwork owner from the user
parent = st.selectbox("Select Parent account", options=accounts)
child = st.selectbox("Select Child account", options=accounts)

contract.functions.transferOwnership(
        parent,
        child
    ).transact({'from': parent})

amount = st.text_input("How much is your chore worth?")

#if st.button("Transfer money"):
if model_result==1:
    # Use the contract to send a transaction to the registerArtwork function

    contract.functions.mint(
        parent,
        int(amount),
    ).transact({'from': parent})

    contract.functions.transfer(
        child,
        int(amount),
    ).transact({'from': parent})
    #receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(f"Allowance of {amount} is transferred from the parent account {parent} to the child account {child}")
    #st.write(dict(receipt))

st.markdown("---")

selected_address = st.selectbox("Select Account", options=accounts)
tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} ")

# token_id = st.selectbox("Artwork Tokens", list(range(tokens)))

#load the model
# file_path=Path('image_model.h5')
# model_load=tf.keras.models.load_model(file_path)

#predict
# predicted=model_load.predict(X_test[-5:])
# df_eval=pd.DataFrame({'prediction':np.argmax(predicted,axis=-1)})
# df_eval['actual']=y_test[-5:]
# plt.plot(df_eval)


        
            
#def analyze_image(image):
#    return True

# show_kitchen_button()

# image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])
# if image_file is not None:
#     file_details = {"FileName": image_file.name, "FileType": image_file.type}
#     result = analyze_image(image_file)
#     if (result):
        
#         st.write(file_details)

##----------- NOT WORKING

# kitchen_button = st.button('Clean Kitchen')
# if kitchen_button:
#     image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])
#     if image_file is not None:
#         file_details = {"FileName": image_file.name, "FileType": image_file.type}
#         st.write(file_details)
 ##----------- NOT WORKING
 #        
# if st.session_state.kitchen_button_disabled == False:
#     kitchen_button = st.button("Clean Kitchen", key='kitchen_button_disabled', disabled=st.session_state.kitchen_button_disabled)
#     if kitchen_button:
#         st.session_state.kitchen_button == False
#         image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])
    

# if st.session_state.kitchen_button == False:
#     image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])
#     if image_file is not None:
#         file_details = {"FileName": image_file.name, "FileType": image_file.type}
#         st.write(file_details)
#         st.session_state.kitchen_button = True
        
#         submit_button = st.button("Analyze") 
#         if submit_button:
#             st.write("Analysis Complete")
#             is_image_good = analyze_image(image_file)
#             if is_image_good:
#                 st.session_state.accepted_image == True
#                 mouse.click('left')
# else:
#     kitchen_button = st.button("Clean Kitchen")
#     if kitchen_button:
#         st.session_state.kitchen_button = False
#         mouse.click('left')
    
    
# @st.cache
# def load_image(image_file):
#     img = Image.open(image_file)
#     return img


# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

# def show_kitchen_button():
#     kitchen_button = st.empty()
#     if kitchen_button.button("Clean Kitchen"):
#         kitchen_button.empty()
#         # image = st.empty()
#         image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])
#         if image_file is not None:
#             file_details = {"FileName": image_file.name, "FileType": image_file.type}
#             st.write(file_details)
#             st.write(type(image_file))
#             img = load_image(image_file)
#             st.image(img, height=250, width=250)
#         # if image.file_uploader("Upload Image", type=["png", "jpg"]):
#         #     with open("file.png", 'wb') as f: 
#         #         f.write(image)