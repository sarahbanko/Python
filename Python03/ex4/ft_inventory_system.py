import sys


def store_data() -> dict[str, int]:
    data = {}
    total_argv = len(sys.argv)

    i = 1
    while i < total_argv:
        item = sys.argv[i].split(":")

        if len(item) != 2 or not item[0]:
            print(f"Error - invalid parameter '{sys.argv[i]}'")

        elif item[0] in data:
            print(f"Redundant item '{item[0]}' - discarding")

        else:
            try:
                data[item[0]] = int(item[1])
            except ValueError as error:
                print(f"Quantity error for '{item[0]}': {error}")

        i += 1

    return data


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = store_data()
    print(f"Got inventory: {inventory}")

    items = list(inventory)
    print(f"Item list: {items}")

    sum_items = sum(inventory.values())
    len_items = len(inventory)
    print(f"Total quantity of the {len_items} items: {sum_items}")

    if inventory:
        most_item = items[0]
        less_item = items[0]

        for item in inventory:
            if sum_items != 0:
                percentage = (inventory[item] / sum_items) * 100
                print(f"Item {item} represents {percentage:.1f}%")

            if inventory[item] > inventory[most_item]:
                most_item = item

            if inventory[item] < inventory[less_item]:
                less_item = item

        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {less_item} "
            f"with quantity {inventory[less_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")