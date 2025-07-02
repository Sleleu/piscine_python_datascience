import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.array:
    """
    Load an image, print its format and its pixel content in RGB format.

    Parameters:
    - path (str): Path to the image file.

    Returns:
    - Image data in a numpy array or None in case of error.
    """
    HANDLED_ERRORS = (FileNotFoundError, PermissionError,
                      AttributeError, IsADirectoryError,
                      UnidentifiedImageError)
    try:
        with Image.open(path) as image:
            img_data = np.array(image)
            print(f"The shape of image is: {img_data.shape}")
            return img_data
    except HANDLED_ERRORS as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        return None
