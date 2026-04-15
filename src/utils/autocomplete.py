from prompt_toolkit.completion import Completer, Completion


class StudentCompleter(Completer):
    def __init__(self, students, used_students):
        self.students = students
        self.used_students = used_students

    def get_completions(self, document, complete_event):
        text = document.text.lower()

        if not text:
            return

        for s in self.students:
            # 🔥 skip déjà utilisés
            from src.utils.text import clean_name
            if clean_name(s) in self.used_students:
                continue

            if s.lower().startswith(text):
                yield Completion(s, start_position=-len(text))