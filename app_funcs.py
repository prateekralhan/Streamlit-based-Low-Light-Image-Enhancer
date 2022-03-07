from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import streamlit as st
from huggingface_hub import from_pretrained_keras


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def instantiate_model():
    model = from_pretrained_keras("keras-io/lowlight-enhance-mirnet", compile=False)
    return model


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def enhance_image(uploaded_image, downloaded_image):
    model = instantiate_model()
    low_light_img = Image.open(uploaded_image).convert('RGB')
    #width, height = low_light_img.size
    #low_light_img = low_light_img.resize((256,256),Image.NEAREST)

    image = img_to_array(low_light_img)
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis = 0)

    output = model.predict(image)
    output_image = output[0] * 255.0
    output_image = output_image.clip(0,255)

    output_image = output_image.reshape((np.shape(output_image)[0],np.shape(output_image)[1],3))
    output_image = np.uint32(output_image)
    final_image = Image.fromarray(output_image.astype('uint8'),'RGB')
    final_image.save(downloaded_image)


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')
