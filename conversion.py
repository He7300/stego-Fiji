import numpy as np
from PIL import Image as im


def main():
    # Load the numpy array from an npy file
    array = np.load('here.png.npy')
    array = array.astype('uint8')

    # Check type of array
    print(type(array))

    # Show the shape of the array
    print(array.shape)

    # Show the array
    print(array)

    # Creating image object of above array
    data = im.fromarray(array)

    # Saving the final output as a PNG file
    data.save('output.png')


if __name__ == "__main__":
    # Function call
    main()
