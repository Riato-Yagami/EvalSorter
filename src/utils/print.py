import sys

def live_status(i, total_pages, bar, remaining, name=None):
    base = f"📄 {i}/{total_pages}  |  {bar}  |  ⏳ {remaining}"

    if name:
        base += f"  |  ✏️ {name}"

    sys.stdout.write("\r" + base)
    sys.stdout.flush()