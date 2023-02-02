from cProfile import label
import streamlit as st
from PIL import Image
from skin_disorder_detection.detect_disorder import process_image
import cv2
import numpy as np

#st.set_page_config(page_title="Enter New Record", page_icon="🖊️")

def load_image(image_file):
	img = Image.open(image_file)
	return img

def show_image(RESULTS_DIR = 'img_results/result.jpg'):
            
            st.header("Processed Image")
            st.image(RESULTS_DIR)

# def get_thresh(img,thresh_default=25):
    
#     thresh = st.slider('Please enter threshhold value ', 0, 255, thresh_default)
#     st.write("Selected threshold value is", thresh)
#     update_image(img,thresh)
    
# def update_image(img,thresh=25):
    
#     res,image,out_path = process_image(img,thresh)
    
#     show_result(res)
#     show_image(image)


if "logged_in_user" in st.session_state:

    body_part = st.selectbox(
        'Select Body Part',
        ('Face', 'Hands', 'Legs'))

    date = st.date_input("Date")
    st.subheader("Image")
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    if image_file is not None:
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        process_image(image,body_part,date)
        #st.button(label = 'save', help='press to generate results for the Image', on_click =save,args=((image,body_part,date),))
        
        
    if image_file is not None:

        # To See details
        file_details = {"filename":image_file.name, "filetype":image_file.type,
                        "filesize":image_file.size}
       # st.write(file_details)

        # To View Uploaded Image
     


else:
    st.header("Please Login!")

