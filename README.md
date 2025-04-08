# imageResize
Python program to adjust image files to meet upload requirements for different services, such as Salesforce. Can resize and/or change quality in order to reduce file size.

Can configure the max size you want your file to be in KB, quality decrement for each iteration until size requirements are met, and max dimensions
example:
INPUT_FOLDER = "Path\\to\\photos"
OUTPUT_FOLDER = "output\\folder"
MAX_SIZE_KB = 250
MAX_DIMENSION = 3500
QUALITY_DECREMENT = 5
