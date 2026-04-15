from PyPDF2 import PdfReader
import fitz  # PyMuPDF
from pdf2image import convert_from_path


def load_pdf_reader(path):
    return PdfReader(path)


def load_pdf_doc(path):
    return fitz.open(path)


def load_page_image_pdf(doc, i):
    page = doc[i]
    pix = page.get_pixmap()

    import numpy as np
    import cv2

    img = np.frombuffer(pix.samples, dtype=np.uint8)
    img = img.reshape(pix.height, pix.width, pix.n)

    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    return img


def load_page_image_img(path, i, dpi):
    images = convert_from_path(
        path,
        first_page=i + 1,
        last_page=i + 1,
        dpi=dpi
    )
    return images[0]