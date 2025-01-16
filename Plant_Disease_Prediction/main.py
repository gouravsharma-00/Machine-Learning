import streamlit as st
from PIL import Image
import pandas as pd
import joblib
import numpy as np
import tensorflow as tf

#Load the Model
model = joblib.load("Plant_Disease_Prediction/plant.pkl")

st.title("Plant Disease Prediction Model")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    print("--------------------------------->",img)
    st.image(img, caption="Uploaded Image", use_column_width=True)



l = ['Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

#Prediction
if st.button("Predict"):

    fruits = tf.keras.utils.load_img(uploaded_file,target_size=(180,180))
    print(fruits)
    arr = tf.keras.utils.img_to_array(fruits)
    arr = tf.expand_dims(arr, 0)
    prediction = model.predict(arr)
    s = tf.nn.softmax(prediction[0])
    
    b= l[np.argmax(s)]
    print(b)
    st.write(b)