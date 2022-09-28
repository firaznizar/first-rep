import streamlit as st
import base64
import requests
from PIL import Image
import io

#################################
#need full functions
def get_prediction(image_data):
  #replace your image classification ai service URL
  url = 'https://askai.aiclub.world/890fdc2e-3c12-4c03-8b5f-7f5d9da5c40e'
  r = requests.post(url, data=image_data)
  response = r.json()['predicted_label']
  #score = r.json()['score']
  #print("Predicted_label: {} and confidence_score: {}".format(response,score))
  return response

#################################
#creating the web app

#title for the web app
st.title("🐱 Cats & Dogs Classifier 🐶")

#subheader
st.subheader("About the project..")
#write elements 
st.write("**This web can be used to classify images of cats and dogs. AI was trained in Navigator with AI Club datasets.**")

#showing cats images
st.image("cats.jpg", caption = "Picture of cats")

#showing dogs images
st.image("dogs.jpg", caption = "Picture of dogs")

# #as columns
# col1, col2 = st.columns(2)

# with col1:
#     st.image("cats.jpg", caption = "Picture of cats")
# with col2:
#     st.image("dogs.jpg", caption = "Picture of dogs")

#file uploading and prediction part

image = st.file_uploader(label="Upload an image",accept_multiple_files=False, help="Upload an image to classify them")
if image:
    #converting the image to bytes
    img = Image.open(image)

    #image to be predicted
    st.image(img, caption = "Image to be predicted")

    #converting the image to bytes
    buf = io.BytesIO()
    img.save(buf,format = 'JPEG')
    byte_im = buf.getvalue()

    #converting bytes to b64encoding
    payload = base64.b64encode(byte_im)

    #file details
    file_details = {
      "file name": image.name,
      "file type": image.type,
      "file size": image.size
    }

    #write file details
    st.write(file_details)

    #predictions
    response = get_prediction(payload)

    #prediction label
    st.markdown("This is a **{}**".format(response.split('s')[0]))
