import streamlit as st
import tempfile

from rembg import remove
from PIL import Image


def main():
    st.title("Background Removal App")
    uploaded_file = st.file_uploader(
        "Upload an Image", type=["png", "jpg", "jpeg"], key="uploader"
    )
    if uploaded_file is not None:
        remove_bg(uploaded_file)
        st.success("Background removed successfully!")
        st.image(tempfile.gettempdir() + "/output.png", caption="Processed Image")


def remove_bg(input_path: str):
    input = Image.open(input_path)
    output = remove(input)
    output.save(tempfile.gettempdir() + "/output.png")
    return tempfile.gettempdir() + "/output.png"


if __name__ == "__main__":
    main()
