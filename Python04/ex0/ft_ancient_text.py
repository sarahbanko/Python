import sys


def open_file() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{sys.argv[1]}': {error}")
        return

    try:
        content = file.read()
        print("---\n")
        print(content, end="")
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")
    finally:
        file.close()
        print("\n")
        print("---")
        print(f"File '{filename}' closed.")


if __name__ == "__main__":
    open_file()