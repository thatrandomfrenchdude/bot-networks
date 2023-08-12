# defines the world in which the ants live
# 10 x 10 x 10 cube
class World:
    def __init__(self) -> None:
        self.space = [[[0 for z in range(10)] for y in range(10)] for x in range(10)]  # 100 cube world
        self.food = 100
