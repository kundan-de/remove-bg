# remove-bg

A simple tool to remove the background from images.

## About

**remove-bg** is a Python-based project with a Streamlit front end that allows you to upload images, remove their backgrounds, and download the processed results. This is useful for preparing images for presentations, e-commerce, or graphic design.

## Requirements

- Python
- pip
- [rembg](https://github.com/danielgatis/rembg) library
- [streamlit](https://streamlit.io/)

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Pre-commit Hooks

To ensure code quality, set up pre-commit hooks:

1. Install pre-commit:

    ```bash
    pip install pre-commit
    ```

2. Install the hooks:

    ```bash
    pre-commit install
    ```

## How to Use

1. Start the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. In your browser, upload an image using the provided interface.
3. The app will process the image and provide a download link for the result.

All image uploads and downloads are handled through the Streamlit interface.

## Example

- Upload `photo.jpg` via the Streamlit app.
- Download the processed image (e.g., `output.png`) from the app after background removal.

## License

This project is licensed under the MIT License.
