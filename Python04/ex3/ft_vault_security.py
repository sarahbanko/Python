from sys import stderr


def secure_archive(
        filename: str, 
        action: str = "read", 
        content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
            return True, data

        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return True, "File written successfully"
        else:
            return False, "Invalid action"
    except OSError as error:
        return False, stderr(error)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, content = secure_archive("ancient_fragment.txt")
    print((success, content))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive("new_fragment.txt", "write", content))
