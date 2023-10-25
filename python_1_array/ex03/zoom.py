import numpy as np
from PIL import Image
from load_image import ft_load

def main():
    img_array = ft_load("animal.jpeg")
    print(img_array)
    img_zoom = img_array[100:500, 450:850, 0]
    img_zoom = img_zoom[:,:,np.newaxis]
    print(f"New shape after slicing : {img_zoom.shape}")
    img = Image.fromarray(img_zoom.squeeze(), mode='L')
    img.show()
    print(img_zoom)


if __name__ == "__main__":
    main()