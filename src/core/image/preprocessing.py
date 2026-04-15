import cv2
import numpy as np


def preprocess_image(pil_image):
    import cv2
    import numpy as np

    img = np.array(pil_image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # agrandissement = énorme boost OCR
    gray = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # suppression bruit
    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # binarisation propre
    th = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        7
    )

    return th