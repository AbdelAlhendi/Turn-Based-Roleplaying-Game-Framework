# from Player import Player
#

class Weapon:
    """
    A weapon to be wielded by the Player
    Abstract Data Type

    Attributes:
        weapon_dmg: the weapon's damage value
        offhand: True if the weapon can only be equipped in the offhand
        is_mainhand: True if the weapon is currently equipped in the mainhand
    """
    weapon_dmg: int
    offhand: bool
    is_mainhand: bool
    # player: Player

    def __init__(self, dmg: int, offhand: bool = False) -> None:
        self.weapon_dmg = dmg
        self.offhand = offhand
        self.is_mainhand = False
        # self.player = None

    def __str__(self) -> str:
        return "Weapon"

    def description(self) -> str:
        return "Weapon"

    def active(self) -> None:
        raise NotImplementedError("To Be Implemented in Subclass")

    def passive(self) -> None:
        raise NotImplementedError("To Be Implemented in Subclass")


class WoodenSword(Weapon):
    """
    A simple and weak wooden sword
    """

    def __init__(self) -> None:
        super().__init__(10)

    def __str__(self) -> str:
        return "Wooden Sword"

    def description(self) -> str:
        return "More of a stick than a sword. Nonetheless, it's preferable " \
               "to one's bare fists. Might leave the user with splinters!"
