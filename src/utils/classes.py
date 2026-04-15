import os
import re

from src.utils.text import normalize


def extract_class_name(filename):
    name = filename.upper()

    # enlève extension
    name = re.sub(r"\.PDF$", "", name)

    # cherche patterns type :
    # B.6C, B-6C, A.5A, etc.
    match = re.search(r"([A-Z]+)[\.\-]?(\d+[A-Z])", name)

    if match:
        return f"{match.group(1)}.{match.group(2)}"

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