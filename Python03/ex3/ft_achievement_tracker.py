import random


ACHIEVEMENTS = [
                'Crafting Genius', 'Strategist', 'World Savior',  
                'Speed Runner','Survivor', 'Master Explorer',  
                'Treasure Hunter', 'Unstoppable', 'First Steps', 
                'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']

def gen_player_achievements() -> set[str]:

    amount = random.randint(4, 9)
    select = random.sample(ACHIEVEMENTS, amount)

    return set(select)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    all_achievements = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_achievements}\n")

    common_achievements = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_achievements}\n")

    difference_alice = alice.difference(bob, charlie, dylan)
    difference_bob = bob.difference(alice, charlie, dylan)
    difference_charlie = charlie.difference(alice, bob, dylan)
    difference_dylan = dylan.difference(alice, bob, charlie)

    print(f"Only Alice has: {difference_alice}")
    print(f"Only Bob has: {difference_bob}")
    print(f"Only Charlie has: {difference_charlie}")
    print(f"Only Dylan has: {difference_dylan}\n")

    all_possible = set(ACHIEVEMENTS)

    print(f"Alice is missing: {all_possible.difference(alice)}")
    print(f"Bob is missing: {all_possible.difference(bob)}")
    print(f"Charlie is missing: {all_possible.difference(charlie)}")
    print(f"Dylan is missing: {all_possible.difference(dylan)}")
          
          

