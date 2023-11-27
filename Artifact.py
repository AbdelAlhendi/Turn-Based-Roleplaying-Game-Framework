# from Player import Player

class Artifact:
    """
    An artifact to be worn by the Player, provides certain benefits
    Abstract Data Type

    Attributes:
        bonus_hp: bonus health points provided
        bonus_dmg: bonus dmg provided
        bonus_mana: bonus mana provided
        bonus_luck: bonus luck provided
    """
    bonus_hp: int
    bonus_dmg: int
    bonus_mana: int
    bonus_luck: int

    def __init__(self, hp: int = 0, dmg: int = 0, mana: int = 0, luck: int = 0) \
            -> None:
        self.bonus_hp = hp
        self.bonus_dmg = dmg
        self.bonus_mana = mana
        self.bonus_luck = luck

    def __str__(self) -> str:
        return "Artifact"

    def description(self) -> str:
        return "Artifact"

    def active(self) -> None:
        raise NotImplementedError("To Be Implemented in Subclass")

    def passive(self) -> None:
        raise NotImplementedError("To Be Implemented in Subclass")


class VampireNecklace(Artifact):

    def __str__(self) -> str:
        return "Vampire's Necklace"

    def description(self) -> str:
        return "A stolen vial of Vampire's blood attached to a piece of " \
               "string. " \
               "Could be worn as a necklace.\n\nLet's the wearer bathe in" \
               " the blood of their enemies, revitalising them.\n\nThe vial " \
               "was created with the intention of granting eternal life, for" \
               " a vampire's blood is so unholy, it defies even death itself."

    def passive(self) -> None:
        raise NotImplementedError()
