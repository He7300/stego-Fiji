import imagej
import numpy as np


def LSB_encrypt(plain_image, secret_image, output_file):
    # Start the ImageJ instance
    ij = imagej.init()

    # Load the cover and secret message images
    cover = ij.io().open(plain_image)
    secret = ij.io().open(secret_image)

    # Convert the cover and secret message images to numpy arrays
    cover_array = ij.py.from_java(cover)
    secret_array = ij.py.from_java(secret)

    # Truncate the secret message to fit inside the cover image
    max_bits = (cover_array.size // 8) - 1
    secret_bits = np.unpackbits(secret_array)[:max_bits * 8].reshape(-1, 8).transpose()

    # Embed the secret message into the cover image using LSB steganography
    stego_array = cover_array.astype(np.uint8)
    for i in range(len(secret_bits)):
        for j in range(8):
            if i < stego_array.shape[1] and j < stego_array.shape[0]:
                stego_array[j, i] = (stego_array[j, i] & ~1) | secret_bits[j, i]

    # Convert the stego array back to an ImageJ image
    stego = ij.py.to_java(np.transpose(stego_array, (1, 2, 0)))

    # Show the stego image in a Fiji/ImageJ window
    ij.py.show(stego)

    # Wait for the user to close the window
    ij.ui().show('Stego image')

    # Save the stego image to a file
    stego_path = output_file
    fs = ij.io.FileSaver(ij.py.to_java(stego))
    fs.saveAsPng(stego_path)

    # Stop the ImageJ instance
    ij.dispose()

if __name__ == '__main__':
    LSB_encrypt("cover.bmp", "duck.jpg", "here.jpg")
