#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("arquivo.txt")
    elif operation_number == 3:
        10 + "a"
    else:
        return


def test_error_typer() -> None:
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully")
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_typer()
