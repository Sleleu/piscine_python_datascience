import numpy as np
from PIL import Image
from load_image import ft_load


def zoom(img: np.array, bd: list) -> np.array:
    """
    Resize and extract a portion of an image.

    :param img: An image as a NumPy array.
    :param bd: A list [h1, h2, w1, w2] defining the coordinates
               of the area to extract.
    :return: A new extracted and resized image as a NumPy array.
    """
    img_zoom = img[bd[0]:bd[1], bd[2]:bd[3], 0]
    img_zoom = img_zoom[:, :, np.newaxis]
    print(f"New shape after slicing : {img_zoom.shape}", end="")
    print(f" or ({img_zoom.shape[0]}, {img_zoom.shape[1]})")
    return img_zoom


def main():
    """
    Main function to load an image, perform zoom, and display it.

    Loads an image from a file, applies the 'zoom' function to extract
    and resize a part of the image, and displays this zoomed part in grayscale.

    :return: A return code (1 in case of error, otherwise None).
    """
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)
        img_zoom = zoom(img_array, [100, 500, 450, 850])
        img = Image.fromarray(img_zoom.squeeze(), mode='L')
        img.show()
        print(img_zoom)
    except TypeError as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        return 1


if __name__ == "__main__":
    main()
