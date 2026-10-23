import sys


def print_sys() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    total = len(sys.argv)

    if total == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total - 1}")

        i = 1
        while i < total:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {total}")


if __name__ == "__main__":
    print_sys()
