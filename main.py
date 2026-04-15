import os
import cv2

from PyPDF2 import PdfWriter

from config import INPUT_DIR, OUTPUT_DIR, VIEW_MODE, PDF_DPI

from src.core.pdf.loader import (
    load_pdf_reader,
    load_pdf_doc,
    load_page_image_pdf,
    load_page_image_img
)

from src.core.image.viewer import show_page

from src.utils.text import clean_name
from src.utils.progress import (
    get_already_processed_pages,
    get_processed_students,
    progress_bar
)

from src.utils.print import live_status

from src.utils.classes import load_students_for_file

from prompt_toolkit import prompt
from src.utils.autocomplete import StudentCompleter


def process_file(file):
    path = os.path.join(INPUT_DIR, file)
    base = os.path.splitext(file)[0]

    print("\n========================")
    print(f"📄 Traitement : {file}")
    print("========================")
    print(f"🖥 Mode affichage : {VIEW_MODE}")

    # 👥 chargement élèves
    students = load_students_for_file(file, "input/classes")
    print(f"👥 {len(students)} élèves chargés")

    # 📄 PDF reader
    reader = load_pdf_reader(path)

    # 📄 doc PDF si mode PDF
    if VIEW_MODE == "pdf":
        doc = load_pdf_doc(path)
    else:
        doc = None

    # 📁 output
    output_folder = os.path.join(OUTPUT_DIR, base)
    os.makedirs(output_folder, exist_ok=True)

    # 🔁 reprise
    start_page = get_already_processed_pages(output_folder, base)
    print(f"⏩ Reprise à la page {start_page + 1}")

    # 🧠 élèves déjà traités
    used_students = get_processed_students(output_folder, base)
    print(f"✅ {len(used_students)} élèves déjà traités")

    # 🧾 writers
    eleves = {}

    # ⚡ autocomplete
    completer = StudentCompleter(students, used_students)

    try:
        total_pages = len(reader.pages)

        for i in range(start_page, total_pages):
            page = reader.pages[i]

            remaining = total_pages - i - 1
            bar = progress_bar(i + 1, total_pages)

            # print(f"\n📄 Page {i+1}/{total_pages}  |  {bar}  |  ⏳ reste {remaining}")
            print(f"\n📄 {i+1}/{total_pages} | {bar} | ⏳ {remaining}")

            if VIEW_MODE == "pdf":
                img = load_page_image_pdf(doc, i)
            else:
                img = load_page_image_img(path, i, PDF_DPI)

            show_page(img, i)

            # ✏️ saisie utilisateur
            user = prompt(
                "✏️ Nom prénom : ",
                completer=completer,
                complete_while_typing=True
            ).strip()

            if not user:
                user = "inconnu"

            final = clean_name(user)

            # 🧠 ajoute à la liste des utilisés
            used_students.add(final)

            # 📄 writer
            if final not in eleves:
                eleves[final] = PdfWriter()

            eleves[final].add_page(page)

            # 💾 sauvegarde immédiate
            output_path = os.path.join(output_folder, f"{base}-{final}.pdf")

            with open(output_path, "wb") as f:
                eleves[final].write(f)

            print(f"✅ Page {i+1} sauvegardée → {final}")

            cv2.destroyAllWindows()

    except KeyboardInterrupt:
        print("\n⛔ INTERRUPTION DETECTEE (Ctrl+C)")
        print("💾 Sauvegarde en cours...")

        for name, writer in eleves.items():
            output_path = os.path.join(output_folder, f"{base}-{name}.pdf")

            with open(output_path, "wb") as f:
                writer.write(f)

        print("✅ Sauvegarde terminée")
        return

    print(f"\n🎉 Terminé : {file}")


def main():
    for f in os.listdir(INPUT_DIR):
        if f.endswith(".pdf"):
            process_file(f)


if __name__ == "__main__":
    main()