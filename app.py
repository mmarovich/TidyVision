import streamlit as st
from web3 import Web3
import pandas as pd
from pathlib import Path
#load the model
import tensorflow as tf
from PIL import Image
import mouse


#load the model
# file_path=Path('image_model.h5')
# model_load=tf.keras.models.load_model(file_path)

#predict
# predicted=model_load.predict(X_test[-5:])
# df_eval=pd.DataFrame({'prediction':np.argmax(predicted,axis=-1)})
# df_eval['actual']=y_test[-5:]
# plt.plot(df_eval)

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
        
            
def analyze_image(image):
    return True

# show_kitchen_button()

# image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])
# if image_file is not None:
#     file_details = {"FileName": image_file.name, "FileType": image_file.type}
#     result = analyze_image(image_file)
#     if (result):
        
#         st.write(file_details)

kitchen_button = st.button('Clean Kitchen')
if kitchen_button:
    image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])
    if image_file is not None:
        file_details = {"FileName": image_file.name, "FileType": image_file.type}
        st.write(file_details)
        
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