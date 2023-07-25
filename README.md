# PDFX - Encrypter and Decrypter


PDF Encrypter and Decrypter is a simple GUI application built with Python and Tkinter for encrypting and decrypting PDF files using the PyPDF2 library.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction
This application allows users to easily encrypt and decrypt PDF files with a password using a graphical user interface (GUI). The GUI is created using the Tkinter library, providing a straightforward way for users to interact with the program.

## Requirements
To use this application, you need the following:
- Python 3.7, 3.8, or 3.9 (other Python 3 versions may also work, but they haven't been tested)
- PyPDF2 library (`pip install PyPDF2`)

## Installation
1. Clone this repository to your local machine or download the ZIP file and extract it.
2. Install the required libraries by running the following command:
   
** pip install PYPDF2

3. Navigate to the repository's directory.

## Usage
Run the `pdf_encrypter_decrypter.py` script to launch the GUI application.

1. **Encrypt PDF File**:
- Click the "Browse" button to select the PDF file you want to encrypt.
- Enter a password in the "Enter Password" field.
- Click the "Encrypt" button to start the encryption process.
- The encrypted PDF will be saved with a new name in the chosen location.

2. **Decrypt PDF File**:
- Click the "Browse" button to select the encrypted PDF file you want to decrypt.
- Enter the correct password in the "Enter Password" field.
- Click the "Decrypt" button to start the decryption process.
- The decrypted PDF will be saved with a new name in the chosen location.

**Note**: If the selected PDF file is already encrypted during encryption or is not encrypted during decryption, appropriate error messages will be displayed.



