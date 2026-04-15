import os
import re

from src.utils.text import normalize


def extract_class_name(filename):
    name = filename.upper()

    # enlève extension
    name = re.sub(r"\.PDF$", "", name)

    # enlève préfixes type E-3-, E-12-, etc.
    name = re.sub(r"^[A-Z]-\d+-", "", name)

    # normalise tirets
    name = name.replace("-", ".")

    # 1️⃣ cas type M.6MATHS2 / B.6C / A.5A
    match = re.search(r"([A-Z]{1,3})\.?(\d+[A-Z0-9]*)", name)
    if match:
        return f"{match.group(1)}.{match.group(2)}"

    # 2️⃣ fallback type MATHS2 seul
    match = re.search(r"([A-Z]{3,}\d+)", name)
    if match:
        return match.group(1)

    return None

def load_students_for_file(filename, classes_folder):
    class_name = extract_class_name(filename)

    if not class_name:
        return []

    path = os.path.join(classes_folder, f"{class_name}.txt")

    students = []

    if not os.path.exists(path):
        print(f"⚠ Classe introuvable : {class_name}")
        return students

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                students.append(line)

    return students

def suggest_students(input_text, students, limit=5):
    input_text = normalize(input_text)

    matches = []

    for s in students:
        if normalize(s).startswith(input_text):
            matches.append(s)

    return matches[:limit]