import streamlit as st 
from PIL import Image
from classify_120_streamlit import predict
import time

st.title("Dog Breed Classifier")

uploaded_file = st.file_uploader("Choose an image...")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Identifying Dog Breed...")
    with st.spinner('Wait for it...'):
        time.sleep(5)
        label, probability = predict(uploaded_file)
        st.write('Predicted class for the input image is %s with probability %.2f percent' % (label, probability),'success')
        st.balloons()
    st.success('Done!')    