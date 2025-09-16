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

        img = open(tempfile.gettempdir() + "/output.png", "rb").read()
        st.download_button(
            label="Download Image", data=img, file_name="output.png", mime="image/png"
        )
    else:
        st.info("Please upload an image to remove its background.")


def remove_bg(input_path: str):
    """Remove background from the image and save the output."""
    input = Image.open(input_path)
    output = remove(input)
    output.save(tempfile.gettempdir() + "/output.png")


if __name__ == "__main__":
    main()
