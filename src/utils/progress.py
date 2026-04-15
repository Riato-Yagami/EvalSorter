import os


def get_already_processed_pages(output_folder, base):
    if not os.path.exists(output_folder):
        return 0

    files = [
        f for f in os.listdir(output_folder)
        if f.startswith(base) and f.endswith(".pdf")
    ]

    return len(files)


def get_processed_students(output_folder, base):
    students = set()

    if not os.path.exists(output_folder):
        return students

    for f in os.listdir(output_folder):
        if f.startswith(base) and f.endswith(".pdf"):
            name = f.replace(f"{base}-", "").replace(".pdf", "")
            students.add(name)

    return students

def progress_bar(current, total, size=20):
    ratio = current / total
    filled = int(ratio * size)
    bar = "█" * filled + "░" * (size - filled)
    percent = int(ratio * 100)
    return f"{bar} {percent}%"