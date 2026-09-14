#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    temp = "25"
    print(f"Input data is '{temp}'")

    temperature = input_temperature(temp)
    print(f"Temperature ir now {temperature}°C")

    temp = "abc"
    print(f"Input data is '{temp}'")

    try:
        input_temperature(temp)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
