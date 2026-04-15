import cv2
import numpy as np

from config import (
    PREVIEW_WIDTH,
    PREVIEW_HEIGHT,
    PREVIEW_CROP_TOP,
    PREVIEW_CROP_BOTTOM,
    PREVIEW_CROP_LEFT,
    PREVIEW_CROP_RIGHT
)


def show_page(image, page_number):
    img = np.array(image)

    # RGB -> BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    h, w = img.shape[:2]

    # ----------------------------
    # CROP ZONE PARAMÉTRABLE
    # ----------------------------
    y1 = int(h * PREVIEW_CROP_TOP)
    y2 = int(h * PREVIEW_CROP_BOTTOM)
    x1 = int(w * PREVIEW_CROP_LEFT)
    x2 = int(w * PREVIEW_CROP_RIGHT)

    img = img[y1:y2, x1:x2]

    # ----------------------------
    # RESIZE POUR AFFICHAGE
    # ----------------------------
    img = cv2.resize(img, (PREVIEW_WIDTH, PREVIEW_HEIGHT))

    cv2.imshow(f"Page {page_number + 1}", img)
    cv2.waitKey(1)