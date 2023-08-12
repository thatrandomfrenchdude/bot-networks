import uuid


# defines the generic ant class
class Ant:
    def __init__(self, role: str) -> None:
        self.id = uuid.uuid4()
        self.role: str = role


# defines the leader ant
# should always be outnumbered by workers 9 to 1
class Leader(Ant):
    def __init__(self) -> None:
        super().__init__('leader')
        self.rules: dict = {}
        self.energy = 6
        self.food = 0


# defines the worker ant
# should outnumber leader 9 to 1
class Worker(Ant):
    def __init__(self) -> None:
        super().__init__('worker')
        self.rules: dict = {}
        self.energy = 10


def generate_troop() -> list:
    troop = [Leader()]
    troop.extend([Worker() for _ in range(9)])
    return troop
