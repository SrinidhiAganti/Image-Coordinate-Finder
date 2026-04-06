import streamlit as st
from PIL import Image

st.title("🖼️ PixelMap - Image Coordinate Finder")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_column_width=True)

    st.write("Click coordinates manually (example input):")

    x = st.number_input("X Coordinate", min_value=0)
    y = st.number_input("Y Coordinate", min_value=0)

    if st.button("Save Coordinate"):
        st.success(f"Saved Coordinate: ({x}, {y})")
