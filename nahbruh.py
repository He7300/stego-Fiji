import imagej
import numpy as np
from PIL import Image

def LSB_decrypt(stego_path, output_file):
    # Start the ImageJ instance
    ij = imagej.init()

    # Load the stego image
    stego = ij.io().open(stego_path)

    # Convert the stego image to a numpy array
    stego_array = ij.py.from_java(stego)

    # Extract the LSBs from the stego array to recover the secret message
    secret_bits = np.packbits(stego_array & 1).flatten()[:((stego_array.size // 8) - 1) * 8]

    # Convert the secret message back to bytes and save to a file
    secret_array = secret_bits.reshape(-1, 8).transpose()[0]
    secret = bytes(secret_array)
    with open(output_file, 'wb') as f:
        f.write(secret)

    # Stop the ImageJ instance
    ij.dispose()