# Author: Nicholas Debeurre (nick.debeurre@aicadium.ai)
import multiprocessing
import uuid

from world import World
from ant import generate_troop

# Ant Farm: The idea here is to have a subset minority of a process pool delegating tasks
# and a subset majority working on tasks. The majority will "vote" as needed.
# in other words, the Leader cannot act without input from the followers.
# the leader exists to execute the will of the majority

# how can followers provide input?


# task:
# collect all food units in the world while minimizing the energy expended

# rules:
# all ants except leader must move one square each turn
# an ant dies if it reaches 0 energy
# what does the leader do?

# physics
# moving one square costs 1 energy unit
# one food unit replenishes 2 energy units

def main() -> None:
    world: World = World()
    troop = generate_troop()

    for ant in troop:
        print(f"Ant {ant.id} is a {ant.role}")


if __name__ == '__main__':
    main()
