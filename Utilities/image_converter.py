'''
Real World Application:
- Enable photo imports to accurately show date created in Apple Photos or MS Photos album
- These programs sort by 'date taken' which is an EXIF data attribute
- This applies to most screenshots, downloaded images, and any format outside of JPEG & TIFF

Roadmap:
[X] Set up both sys.argv and use input if no argument is given
[X] Set up help menu and exit functionality
[X] Validate the source directory is found
[X] Create the output directory for modified images
[X] Sort out non-JPEG & TIFF images (EXIF unsupported) into a secondary folder
[ ] Modify sort to capture 'Date Modified' before saving to a variable
[ ] Convert photo to .jpeg and apply exif 'Date Taken' as 'Date Modified'
'''


import os
import sys
from PIL import Image

IMAGE_EXTENSIONS = '.png', 'jpg'
HELP_MENU = '''
Method 1:
python image_converter.py

Method 2:
python image_converter.py <target_directory>
'''


def get_input():
    directory = input('What is the source directory? ')
    if directory.lower() == 'help':
        print(HELP_MENU)
        main()
    elif directory.lower() == 'exit':
        sys.exit(1)
    return directory


def validate_directory(input_dir):
    if not os.path.exists(input_dir):
        print("Path not found. Please check your input path\n")
        sys.argv = [sys.argv[0]]
        main()
    if input_dir[-1] != '/':
        source_dir = input_dir + '/'
    return source_dir


def create_ouput_directory(input_dir):
    output_dir = f'{input_dir}converted_images/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    return output_dir


def sort_photos(source_dir, output_dir):
    files = [file for file in os.listdir(source_dir) if file.lower().endswith(IMAGE_EXTENSIONS)]
    for file in files:
        image = Image.open(f'{source_dir}{file}')
        new_image_name = f'{os.path.splitext(file)[0]}.jpeg'
        image.save(f'{output_dir}{new_image_name}', "jpeg")


def main():
    if len(sys.argv) == 2:
        input_dir = sys.argv[1]
    else:
        input_dir = get_input()

    source_dir = validate_directory(input_dir)
    output_dir = create_ouput_directory(source_dir)
    sort_photos(source_dir, output_dir)


if __name__ == "__main__":
    print("\nYou can type 'Help' or 'Exit' at any point.")
    main()
