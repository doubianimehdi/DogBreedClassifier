import streamlit as st 
from PIL import Image
from classify_120_streamlit import predict
from numba import cuda
import time

#import tensorflow as tf
#physical_devices = tf.config.experimental.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

st.title("Dog Breed Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    cuda.select_device(0)
    cuda.close()
    st.write("")
    st.write("Identifying Dog Breed...")
    with st.spinner('Wait for it...'):
        time.sleep(5)
        label = predict(uploaded_file)
        st.write('Predicted Breed : %s' % (label))
        st.balloons()
    st.success('Done!')    