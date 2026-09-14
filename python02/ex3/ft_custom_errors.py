#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknow water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_erros() -> None:
    print("=== Custom Garden Errors ===")

    print("Testing PlantError...")
    try:
        check_plant()
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("Testing WaterError...")
    try:
        check_water()
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        check_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_erros()
