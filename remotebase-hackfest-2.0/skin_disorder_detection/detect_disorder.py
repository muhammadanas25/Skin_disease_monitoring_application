
from utils import get_threshold, remove_background
import cv2
import os
from rembg import remove
import streamlit as st
from db import INSERT_DATA, insert_data
from datetime import datetime

# Parse Arguments
# json_data = json.loads(sys.argv[1])
IMAGE_ID = "222"  # json_data['image_id'] if 'image_id' in json_data else None
img = (
    "./v3.jpg"  # json_data['img'] if 'img' in json_data else None
)


# *** Segmentation Steps ***#

# 1. Open Image
def process_image(img,bodypart,date):
    THRESH_VAL = None # json_data['thresh_val'] if 'thresh_val' in json_data else None
    max=255
    OUT_DIR = "img_results"  # json_data['out_dir'] if 'out_dir' in json_data else 'result'

    BG_RM = True
    #image = img[0]
    
    image= img
    # print(image.shape)
    if BG_RM:
        image = remove(image)
       
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        cv2.imwrite("removed_bg_out_path.jpg", image)

    # 2. Image:Adjust:Size
    # image  = resize_img(image)

    # 3. Image: Color: Split Channel
    # 4. Use Blue channel
    blue_channel, _, _ = cv2.split(image)
    #blue_channel = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    # 5. Image: Adjust: Threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh_bg_img = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh_bg_img = cv2.erode(thresh_bg_img, None, iterations=2)
    thresh_bg_img = cv2.dilate(thresh_bg_img, None, iterations=2)

    # Remove Background
    bg_removed = remove_background(blue_channel, thresh_bg_img)

    # get threshold ImageJ default algorithm

    if not THRESH_VAL:
        min, _, _ = get_threshold(bg_removed)

    #getting thresh from frontend slider 
    min,max = get_thresh(min)
    # print(THRESH_VAL)

    # 6. Apply Threshold
    ret, thresh_img = cv2.threshold(bg_removed, min, max, cv2.THRESH_BINARY)

    # 7. Analyze: Analyze particle: Overlay (check Display results and summary)
    contours, hierarchy = cv2.findContours(
        thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )
    depigmentation_cnts = [cnt for cnt in contours]


    # 3. Depigmented area demarcated.
    depigmentation_area = sum(cv2.contourArea(cnt) for cnt in depigmentation_cnts)
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 30]
    image = cv2.drawContours(image, contours, -1, (0, 255, 0), 1)


    # 5. Percent depigmentation value.
    contours, _ = cv2.findContours(thresh_bg_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 30]
    total_area = sum(cv2.contourArea(x) for x in contours)
    depigmentation_percentage = (depigmentation_area * 100) / total_area
    # print(f"{depigmentation_percentage:.2f}%")


    # Show Image
    thresh_img = cv2.cvtColor(thresh_img, cv2.COLOR_GRAY2BGR)
    out_path = os.path.join(
        OUT_DIR, f"{st.session_state['logged_in_user']}_{bodypart}_{datetime.strftime(date,'%m-%d-%Y')}.jpg"
    )
    
    #out_dir= f"{usernam}"username date vofypath
    #cv2.imwrite('img_results/result.jpg', image)
  
    # Create response
    res = {
        #"preprocessed_image": out_path,
        "skin disorder ratio": f"{depigmentation_percentage:.2f}%",
        # "partical_analysis": depigmentation_cnts
    }

    # print("img_results/result",res)
   

    show_result(res)
    show_image(cv2.cvtColor(img,cv2.COLOR_BGRA2RGB),cv2.cvtColor(image, cv2.COLOR_BGRA2RGB))
    cv2.imwrite(out_path,cv2.cvtColor(cv2.cvtColor(image, cv2.COLOR_BGRA2RGB), cv2.COLOR_BGRA2RGB))
    # insert_data(INSERT_DATA.format(username = st.session_state["logged_in_user"],
    #             body_part = bodypart,
    #             date = datetime.strftime(date,'%m-%d-%Y'),
    #             disorder_percentage= depigmentation_percentage)
    #              )

    return res,image,out_path

def show_result(result):

    for k,v in result.items():
      st.write(f"{k} : {v}")


def get_thresh(thresh_default=25):
    min, max = st.slider('Please enter threshhold value ', 0, 255, (thresh_default, 255))
    st.write("Selected min threshold value is", min ,"Selected max threshold value is", max )

    return min,max

def show_result(result):

    for k,v in result.items():
      st.write(f"{k} : {v}")

def show_image(input_image,result):

        st.header("Processed Image")
        st.image(result)

    
        # st.header("Input Image")
        # st.image(input_image)

def show_radio():
    choice = st.radio(
    "Background removal",
    ('Yes', 'No'))

    if choice == 'Yes':
        return True
    else:
        return True
   
# def save (username = st.session_state["logged_in_user"] , bodypart , date,depigmentation_percentage):
#      insert_data(INSERT_DATA.format(username = st.session_state["logged_in_user"],
#                 body_part = bodypart,
#                 date = datetime.strftime(date,'%m-%d-%Y'),
#                 disorder_percentage= depigmentation_percentage)
#                  )