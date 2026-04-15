import pytesseract
from config import TESSERACT_PATH, LANG

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def ocr_data(image):
    data = pytesseract.image_to_data(
        image,
        lang=LANG,
        output_type=pytesseract.Output.DICT,
        config="--psm 6"
    )
    
    return data


def ocr_text(image):
    text = pytesseract.image_to_string(
        image,
        lang=LANG,
        config="--psm 6"
    )
    
    return text

import pytesseract


def get_words(image):
    return pytesseract.image_to_data(
        image,
        lang="fra",
        config="--psm 6",
        output_type=pytesseract.Output.DICT
    )