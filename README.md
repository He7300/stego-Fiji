Read Me

This Python script includes two functions to perform image processing tasks using ImageJ library, specifically:

    find_diff(ij, image1_path, image2_path): This function reads two image files and computes the absolute difference between their pixel values. It then displays the difference image in a Fiji/ImageJ window and saves it as a PNG file named "diff.png".

    Encrypt_Least_Significant_Bit(plain_image, secret_image, path_secret=''): This function performs LSB (Least Significant Bit) steganography to embed a secret message image into a cover image. The resulting stego image is displayed in a Fiji/ImageJ window. The function also takes an optional argument to save the stego image to a specified path.

To run the script, make sure that the required libraries (ImageJ, NumPy, PIL) are installed in your Python environment. The script can be run from the command line or an IDE.

The main code block contains an example usage of the find_diff() function. It reads two image files named "cover.bmp" and "output.bmp" from the same directory and passes them as arguments to the function.

Note: The script sets the PATH environment variable to include the path to the Apache Maven binary directory. This is required to run ImageJ in Python. If you encounter issues running the script, make sure that the PATH is set correctly in your system.

Please feel free to modify the code to suit your needs.
