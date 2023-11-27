# from Player import Player
#

class Armor:
    """
    Armor to be worn by the Player, increasing HP
    Abstract Data Type

    Attributes:
        hp: the health points the armor provides the Player
    """
    hp: int

    def __init__(self, hp: int) -> None:
        self.hp = hp

    def __str__(self) -> str:
        return "Armor"

    def description(self) -> str:
        return "Armor"

    def active(self) -> None:
        raise NotImplementedError("To Be Implemented in Subclass")

    def passive(self) -> None:
        raise NotImplementedError("To Be Implemented in Subclass")


class ClothArmor(Armor):
    """
    Simple cloth armor, provides minimal defensive benefits
    """

    def __init__(self) -> None:
        super().__init__(5)

    def __str__(self) -> str:
        return "Cloth Armor"

    def description(self) -> str:
        return "These rags, held together by the cheapest of thread, can " \
               "barely be called armor. May be inflammable."


