import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
    ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    events = gen_event()

    for i in range(1000):
        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    event_list = []

    for i in range(10):
        event_list.append(next(events))

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")