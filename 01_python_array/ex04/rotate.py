from load_image import ft_load
import numpy as np
from PIL import Image


def rotate(img: np.array, shape_img: int) -> np.array:
    """
    Rotate an image represented as a NumPy array.

    This function takes an input image as a NumPy array and rotates
    it by 90 degrees by transposing the image's pixel values.
    It creates a new square image with dimensions 'shape_img x shape_img'
    and returns it as a NumPy array.

    :param img: The input image as a NumPy array.
    :param shape_img: The desired shape of the output square image.
    :return: A rotated image as a NumPy array.
    """
    img_rotate = np.zeros([shape_img, shape_img, 3], dtype=np.uint8)
    try:
        for x in range(shape_img):
            for y in range(shape_img):
                img_rotate[y][x] = img[x][y]
    except IndexError as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        exit(1)
    return img_rotate


def main():
    """
    Main function to load an image, perform a rotation, and display the result.

    Loads an image from a file, extracts a square region from it, rotates
    the region by 90 degrees, and displays the rotated image using PIL.

    :return: 1 in case of error, otherwise 0.
    """
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)
        img_square = img_array[100:500, 450:850]
        img_rotate = rotate(img_square, 400)
        print(f"New shape after Transpose : {img_rotate.shape}")
        print(img_rotate)
        img = Image.fromarray(img_rotate)
        img.show()
    except TypeError as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        return 1
    return 0


if __name__ == "__main__":
    main()
