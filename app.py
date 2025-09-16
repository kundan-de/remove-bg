import tempfile

import streamlit as st
from PIL import Image
from rembg import remove

OUTPUT_FILE = tempfile.gettempdir() + "/output.png"


def main():
    """Main function to run the Streamlit app."""

    st.title("Background Removal App")
    uploaded_file = st.file_uploader(
        "Upload an Image", type=["png", "jpg", "jpeg"], key="uploader"
    )
    if uploaded_file is not None:
        remove_bg(uploaded_file)

        st.success("Background removed successfully!")
        st.image(OUTPUT_FILE, caption="Processed Image")

        img = open(OUTPUT_FILE, "rb").read()
        st.download_button(
            label="Download Image", data=img, file_name="output.png", mime="image/png"
        )
    else:
        st.info("Please upload an image to remove its background.")


def remove_bg(input_path: str):
    """Remove background from the image and save the output."""

    input = Image.open(input_path)
    output = remove(input)
    output.save(OUTPUT_FILE)


if __name__ == "__main__":
    main()
