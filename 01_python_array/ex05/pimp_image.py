import numpy as np
from PIL import Image


def ft_invert(array: np.array) -> np.array:
    """
    Inverts the color of the image received and display it.
    """
    array = np.invert(array)
    img = Image.fromarray(array)
    img.show()


def ft_red(array) -> np.array:
    """
    turns the image to red and display it
    """
    red = array.copy()
    red[..., 1] = 0
    red[..., 2] = 0
    img = Image.fromarray(red)
    img.show()


def ft_green(array) -> np.array:
    """
    turns the image to green and display it
    """
    green = array.copy()
    green[..., 0] = 0
    green[..., 2] = 0
    img = Image.fromarray(green)
    img.show()


def ft_blue(array) -> np.array:
    """
    turns the image to blue and display it
    """
    blue = array.copy()
    blue[..., 0] = 0
    blue[..., 1] = 0
    img = Image.fromarray(blue)
    img.show()


def ft_grey(array) -> np.array:
    """
    turns the image to grey
    """
    r, g, b = array[:, :, 0], array[:, :, 1], array[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    img = Image.fromarray(gray)
    img.show()
