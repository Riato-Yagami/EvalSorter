import os


def save_by_students(eleves, output_folder, base_name):
    os.makedirs(output_folder, exist_ok=True)

    for name, writer in eleves.items():
        path = os.path.join(output_folder, f"{base_name}-{name}.pdf")

        with open(path, "wb") as f:
            writer.write(f)