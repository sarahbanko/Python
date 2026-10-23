import sys


def open_file() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{sys.argv[1]}': {error}")
        return

    try:
        content = file.read()
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")
        return
    finally:
        file.close()

    print("---\n")
    print(content, end="")
    print("\n---")
    print(f"File '{filename}' closed.\n")

    print("Transform data:")
    transformed = content.replace("\n", "#\n")
    if content and not content.endswith("\n"):
        transformed += "#"

    print("---\n")
    print(transformed, end="")
    print("\n---")

    file_input = input("Enter new file name (or empty): ")
    if file_input:
        print(f"Saving data to '{file_input}'")
        try:
            file = open(file_input, "w")
            try:
                file.write(transformed)
            finally:
                file.close()
        except OSError as error:
            print(f"Error saving file '{file_input}': {error}")
        else:
            print(f"Data saved in file '{file_input}'")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    open_file()