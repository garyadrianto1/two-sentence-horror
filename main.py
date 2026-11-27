import os

entry = "I finally taught the house to lock the doors when it hears a stranger's voice. Tonight it locked them while I was still talking."

with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd(), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
