import re


def clean_name(name):
    name = name.strip()

    # nettoyage basique OCR
    name = re.sub(r"\s+", " ", name)

    parts = name.split()

    if not parts:
        return "INCONNU_inconnu"

    # NOM = premier mot
    nom = parts[0]
    nom = re.sub(r"[^a-zA-ZÀ-ÿ\-]", "", nom).upper()

    # PRENOM = reste
    prenom_parts = parts[1:] if len(parts) > 1 else ["inconnu"]

    prenom_clean = []

    for p in prenom_parts:
        p = re.sub(r"[^a-zA-ZÀ-ÿ\-]", "", p)
        if p:
            prenom_clean.append(p.lower())

    prenom = "-".join(prenom_clean) if prenom_clean else "inconnu"

    return f"{nom}_{prenom}"


def normalize(s):
    return s.lower().strip()