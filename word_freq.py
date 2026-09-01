import re
import sys
from collections import Counter
from pathlib import Path


def word_freq(path, top=20):
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    words = re.findall(r"[a-z']+", text)
    return Counter(words).most_common(top)


def main():
    if len(sys.argv) < 2:
        print("Usage: python word_freq.py <file> [top_n]")
        sys.exit(1)
    path = Path(sys.argv[1])
    top = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    for word, count in word_freq(path, top):
        print(f"{count:5d}  {word}")


if __name__ == "__main__":
    main()
