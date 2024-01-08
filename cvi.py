#!/usr/bin/python3
# SZMELC CODE VISUALIZER V1

import os
from PIL import Image
from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_for_filename
from pygments.formatters import ImageFormatter
from io import BytesIO

def create_image_with_code(code_file):
    # Read the code from file
    with open(code_file, 'r') as file:
        code = file.read()

    # Try to guess the lexer based on file content or use a default
    try:
        lexer = guess_lexer(code)
    except:
        lexer = get_lexer_for_filename(code_file, code)

    # Syntax highlighting
    formatter = ImageFormatter(font_name='DejaVu Sans Mono', style='monokai', line_numbers=False)
    code_image = highlight(code, lexer, formatter)

    # Convert to PIL image
    image_stream = BytesIO(code_image)
    image = Image.open(image_stream)

    # Output file path
    output_image = os.path.splitext(code_file)[0] + '.png'

    # Save the image
    image.save(output_image)

# Ask user for the file path
file_path = input("Enter the path of the file to visualize: ")

# Usage
create_image_with_code(file_path)
