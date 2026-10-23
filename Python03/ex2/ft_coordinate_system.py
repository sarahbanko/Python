import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = user_input.split(",")

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(coordinates[0])
        except ValueError as error:
            print(f"Error on parameter '{coordinates[0]}': {error}")
            continue

        try:
            y = float(coordinates[1])
        except ValueError as error:
            print(f"Error on parameter '{coordinates[1]}': {error}")
            continue

        try:
            z = float(coordinates[2])
        except ValueError as error:
            print(f"Error on parameter '{coordinates[2]}': {error}")
            continue

        return (x, y, z)


def ft_tuple(coordinates: tuple[float, float, float]) -> None:
    print(
        f"It includes: X={coordinates[0]}, "
        f"Y={coordinates[1]}, Z={coordinates[2]}")


def distance(coordinate1: tuple[float, float, float], coordinate2: tuple[float, float, float]) -> float:
    x1 = coordinate1[0]
    y1 = coordinate1[1]
    z1 = coordinate1[2]

    x2 = coordinate2[0]
    y2 = coordinate2[1]
    z2 = coordinate2[2]

    distance = math.sqrt((x2-x1)**2 +
                (y2-y1)**2 + (z2-z1)**2)

    return distance


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    ft_tuple(pos1)
    print(f"Distance to center: {distance((0, 0, 0), pos1):.4f}\n")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: {distance(pos1, pos2):.4f}")
