class Item:
    """
    A simple item found throughout the Player's adventure. Can be sold.
    Abstract Data Type

    Attributes:
        value: the monetary worth of the item
    """
    value: int

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return "Item"

    def description(self) -> str:
        return "Item"


class CrackedBones(Item):

    def __init__(self) -> None:
        super().__init__(4)

    def __str__(self) -> str:
        return "Cracked Bones"

    def description(self) -> str:
        return "A pile of cracked bones. Can be sold for a low price."
