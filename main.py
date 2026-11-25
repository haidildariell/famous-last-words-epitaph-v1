import os

EPITAPH = "I said 'hold my beer' to the bear. The bear is still holding it."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 150


def validate_epitaph(text):
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= MAX_LENGTH:
        raise ValueError("epitaph must be 1-150 characters, got %d" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("epitaph must be a single line")
    return cleaned


def write_epitaph(text, path=OUTPUT_PATH):
    validated = validate_epitaph(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validated + "\n")
    return validated


def main():
    written = write_epitaph(EPITAPH)
    print("wrote %d characters to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
