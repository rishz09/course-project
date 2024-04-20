import numpy as np
import cv2
import pandas as pd
import pickle
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# uncomment this if you want to use the Random Forest Classifier (which generalises more as it was trained on augmented dataset)
# file_path = 'rf_aug_best.pkl'

file_path = 'gbc_custom.pkl'
with open(file_path, 'rb') as file:
    clf = pickle.load(file)

st.title('My Digit Recognizer')
st.markdown('''
Try to write a digit!
''')

def custom_transform(x, scale):
    new_x = np.empty(x.shape, dtype=(np.float32))
    for i in range(x.shape[0]):
        temp = np.copy(x[i]).astype(np.float32)
        temp[(temp > 0) & (temp < 200)] = scale
        temp[temp >= 200] = 1
        new_x[i][:][:] = temp.astype(np.float32)

    return new_x

SIZE = 192
mode = st.checkbox("Draw (or Delete)?", True)
canvas_result = st_canvas(
    fill_color='#000000',
    stroke_width=20,
    stroke_color='#FFFFFF',
    background_color='#000000',
    width=SIZE,
    height=SIZE,
    drawing_mode="freedraw" if mode else "transform",
    key='canvas')


if canvas_result.image_data is not None:
    img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
    rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
    st.write('Model Input')
    st.image(rescaled)


if st.button('Predict'):
    test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    test_x = custom_transform(test_x.reshape(1, 28, 28), 0.75)
    
    val = clf.predict(test_x.reshape(1, 28*28))[0]
    st.write(f'Result: {val}')

    df = pd.DataFrame(data=clf.predict_proba(test_x.reshape(1, -1))[0])
    st.bar_chart(df)