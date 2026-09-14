#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:

    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


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

    temp = "100"
    print(f"Input data is '{temp}'")
    try:
        input_temperature(temp)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    temp = "-50"
    print(f"Input data is '{temp}'")
    try:
        input_temperature(temp)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
