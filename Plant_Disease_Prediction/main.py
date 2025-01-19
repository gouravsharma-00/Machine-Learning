import streamlit as st
from PIL import Image
import pandas as pd
import joblib
import numpy as np
import tensorflow as tf

# Load the Model
model = joblib.load("Plant_Disease_Prediction/plant.pkl")

st.title("Plant Disease Prediction Model")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    print("--------------------------------->", img)
    st.image(img, caption="Uploaded Image", use_container_width=True)  # Updated parameter

class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

# Prediction
if st.button("Predict"):
    img = tf.keras.utils.load_img(
        uploaded_file, target_size=(img_height, img_width)
    )
    # print(img)
    img_array = tf.keras.utils.img_to_array(img)

    img_array = tf.expand_dims(img_array, 0) # Create a batch
    # print(img_array)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    st.write(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
    f = class_names[np.argmax(score)]
    # st.write(f)
