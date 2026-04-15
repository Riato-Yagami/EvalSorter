from src.core.ocr.engine import get_words

def is_valid_label(word):
    word = word.lower()
    return "nom" in word or "prenom" in word or "prénom" in word

def crop_header(image):
    h, w = image.shape
    return image[0:int(h * 0.18), 0:w]

def extract_right(data, index, max_dx=250):
    x_ref = data["left"][index]
    y_ref = data["top"][index]
    h_ref = data["height"][index]

    words = []

    for i in range(len(data["text"])):
        w = data["text"][i].strip()
        if not w:
            continue

        x = data["left"][i]
        y = data["top"][i]

        # même ligne
        if abs(y - y_ref) > h_ref * 1.2:
            continue

        # à droite uniquement
        if x > x_ref and (x - x_ref) < max_dx:
            words.append((x, w))

    words.sort(key=lambda t: t[0])

    return " ".join([w for _, w in words]).strip()

def extract_fields(image):
    data = get_words(crop_header(image))

    print(data["text"])
    n = len(data["text"])

    nom = None
    prenom = None

    for i in range(n):
        word = data["text"][i].lower().strip()

        if not word:
            continue

        # nettoyage agressif OCR
        word_clean = word.replace(" ", "")

        # détection robuste
        if "nom" in word_clean:
            nom = extract_right(data, i)

        if "prenom" in word_clean or "prénom" in word_clean:
            prenom = extract_right(data, i)

    return prenom, nom