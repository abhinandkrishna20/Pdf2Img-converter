# PDF to Image Converter

This Python script allows you to convert a PDF document into a series of JPG image files using the PyMuPDF library (also known as fitz).

## Prerequisites

Before you can use this script, you'll need to have the following dependencies installed:

- Python 3.x
- PyMuPDF library (`fitz`)

You can install the PyMuPDF library using pip:

```bash
pip install PyMuPDF
```

## Usage

1. Clone this repository to your local machine or download the Python script.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script using Python:

```bash
python pdf2img.py
```

5. You will be prompted to enter the name of the PDF file you want to convert. Please provide the file name without the ".pdf" extension.

6. The script will create a folder with the same name as your PDF file (if it doesn't already exist) and store the JPG images there.

7. Once the conversion is complete, the script will display a message indicating the folder where the images are stored.

## Example

Suppose you have a PDF file named "document.pdf" that you want to convert. Here's what the script execution might look like:

```
Welcome to the PDF to JPG Converter

Give me the file name: document

Folder created.

Images stored in the folder: document

Conversion complete!
```

## Author

[Abhinand Krishna A](https://www.linkedin.com/in/abhinandkrishna/)


## 📖 License

Rig is licensed under the Apache 2.0 License.
