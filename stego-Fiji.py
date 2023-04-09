
import imagej
import numpy as np
import os
from PIL import Image


def find_diff(ij, image1_path, image2_path):
    image1 = ij.io().open(image1_path)
    image2 = ij.io().open(image2_path)

    # Convert the images to numpy arrays
    array1 = ij.py.from_java(image1)
    array2 = ij.py.from_java(image2)

    # Compute the difference between the two arrays
    diff_array = np.abs(array1 - array2)

    # Convert the difference array back to an ImageJ image
    diff_image = ij.py.to_java(diff_array)

    # Show the difference image in a Fiji/ImageJ window
    ij.py.show(diff_image)

    # Wait for the user to close the window
    ij.ui().show('Difference image')
    pil_image = Image.fromarray(np.uint8(diff_array))
    pil_image.save('diff.png')    # Stop the ImageJ instance
    ij.dispose()

def Encrypt_Least_Significant_Bit(plain_image, secret_image, path_secret=''):
    cover = ij.io().open(plain_image)
    secret = ij.io().open(secret_image)

    # Convert the cover and secret message images to numpy arrays
    cover_array = ij.py.from_java(cover)
    secret_array = ij.py.from_java(secret)
    # Reshape the secret message array to have the same number of dimensions as the cover array
    if len(cover_array.shape) != len(secret_array.shape):
        secret_array = secret_array.reshape(cover_array.shape)
    lsb_result = LSB(cover_array, secret_array)
    # Pad the secret message array with zeros to make its size a multiple of 8
    padding = (8 - (secret_array.size % 8)) % 8
    secret_array = np.concatenate((secret_array, np.zeros(padding, dtype=secret_array.dtype)))


    # Convert the stego array back to an ImageJ image
    stego = ij.py.to_java(lsb_result)

    # # Save the stego image to a file
    # ij.io().save(path_secret, stego)

    # Show the secret message in a Fiji/ImageJ window
    ij.py.show(stego)
    ij.dispose()


def LSB(cover_array, secret_array):
    # Embed the secret message into the cover image using LSB steganography
    stego_array = cover_array.astype(np.uint8)
    secret_bits = np.unpackbits(secret_array).reshape(-1, 8)
    for i in range(len(secret_bits)):
        for j in range(8):
            stego_array[i, j] = (stego_array[i, j] & ~1) | secret_bits[i, j]
    return stego_array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.environ['PATH'] =r'C:\Users\He\Downloads\apache-maven-3.9.1-bin\apache-maven-3.9.1\bin'
    ij = imagej.init()

    # Encrypt_Least_Significant_Bit(plain_image='cover.bmp', secret_image='something.bmp')
    find_diff(ij, "cover.bmp", "output.bmp")
    # find_diff(ij, "cover.bmp", "phonenothing.png")

