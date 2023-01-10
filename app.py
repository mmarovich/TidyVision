import streamlit as st
from web3 import Web3
import pandas as pd
from pathlib import Path
from PIL import Image
import cv2
import os
import glob


w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
        
            
def analyze_image(path):
    img_arr=cv2.imread(path)
    img_arr=cv2.resize(img_arr,(224,224))
    # send image to ML
    # tensor flow should convert file to float32
    # result = machine_learning(imported_model, img_arr)  # result should return True if kitchen is clean / false if kitchen is dirty
    # return result
    return True

def purge_image_folder():
    files = glob.glob(os.path.join('image', '*'))
    for f in files:
        os.remove(f)
        
def save_image(image):
    file_type = image.type.rsplit('/',1)[-1]
    img = Image.open(image_file)
    img.save("image/img."+file_type)
    file_path = "image/img." + file_type
    return file_path


image_file = st.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])

kitchen_button = st.button('Clean Kitchen')
if kitchen_button:
    if image_file:
        purge_image_folder()
        file_path = save_image(image_file)
        result = analyze_image(file_path)
        if result:
            st.write("Congrats, you cleaned the kitchen")
            # perform web3 call to transfer funds.
        else:
            st.write("The kitchen is still dirty. Get back to work")
    else:
        st.write("Please upload an image")