
import imagej
import numpy as np
from PIL import Image

import imagej
import numpy as np
from PIL import Image

def LSB_decrypt2(stego_path, output_file):
    # Start the ImageJ instance
    ij = imagej.init()

    # Open the stego image
    stego = ij.io().open(stego_path)

    # Convert the stego image to a numpy array
    stego_array = ij.py.from_java(stego)

    # Extract the secret message from the stego image using LSB steganography
    max_bits = (stego_array.size // 8) - 1
    secret_bits = np.packbits(np.array([stego_array[j, i] & 1 for i in range(stego_array.shape[1])
                                        for j in range(stego_array.shape[0])][:max_bits * 8])
                              .reshape(-1, 8).transpose())
    # remove trailing null bytes
    secret_bits = secret_bits[:np.where(secret_bits==0)[0][0]]

    # Create the secret message image
    secret_image = Image.frombytes(mode='L', size=(stego.getImgPlus().getWidth(),
                                                   stego.getImgPlus().getHeight()),
                                   data=secret_bits)

    # Save the secret message image to a file
    secret_image.save(output_file)

    # Stop the ImageJ instance
    ij.dispose()


def LSB_decrypt(stego_path, output_file):
    # Start the ImageJ instance
    ij = imagej.init()

    # Load the stego image
    stego = ij.io().open(stego_path)

    # Convert the stego image to a numpy array
    stego_array = ij.py.from_java(stego)

    # Extract the LSBs from the stego array to obtain the secret message
    secret_bits = np.zeros_like(stego_array, dtype=np.uint8)
    for i in range(len(secret_bits)):
        for j in range(8):
            if i < stego_array.shape[1] and j < stego_array.shape[0]:
                secret_bits[j, i] = stego_array[j, i] & 1

    # Convert the secret message back to an array of bytes
    secret_bytes = np.packbits(secret_bits.transpose())

    # Save the secret message to a file
    with open(output_file, 'wb') as f:
        f.write(secret_bytes)

    # Stop the ImageJ instance
    ij.dispose()


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
    stego = ij.py.to_java(stego_array)

    # Show the stego image in a Fiji/ImageJ window
    ij.py.show(stego)

    # Wait for the user to close the window
    ij.ui().show('Stego image')

    # Save the stego image to a file
    pil_image = Image.fromarray(np.uint8(stego_array))
    pil_image.save('phonenothing.png')

    # Stop the ImageJ instance
    ij.dispose()

def remove_zeros(file_in, file_out):
    # Read the raw data of the input file
    with open(file_in, 'rb') as f:
        data = f.read()

    # Remove all the 00 bytes from the data
    new_data = bytes(filter(lambda x: x != 0x00, data))

    # Write the new data to the output file
    with open(file_out, 'wb') as f:
        f.write(new_data)

if __name__ == '__main__':
    # LSB_encrypt("cover.bmp", "duck.jpg", "here.jpg")
    # LSB_decrypt(stego_path='here2.bmp', output_file="nahbruh.png")
    # LSB_decrypt(stego_path='phonenothing.png',  output_file="secret_message.png")
    remove_zeros('secret_message.png', 'this.png')