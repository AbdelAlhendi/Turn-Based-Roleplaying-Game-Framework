import random
from typing import Optional
from Armor import Armor
from Artifact import Artifact
from Weapon import Weapon, WoodenSword


class Monster:
    """
    Abstract Data Type
    A monster to be fought by the Player

    Attributes:
        hp: the monster's health points, the monster dies when this goes to 0
        attack: the moonster's attack stat, multiples the damage from attacks
        name: the monster's name
        drops: the items dropped on death
        exp_drop: the amount of exp points dropped on death
    """
    hp: int
    attack: float
    name: str
    drops: Weapon
    exp_drop: int

    def __init__(self, hp: int, attack: float, name: str, exp_drop: int) -> None:
        self.hp = hp
        self.attack = attack
        self.name = name
        self.exp_drop = exp_drop

    def __str__(self) -> str:
        return self.name

    def skill1(self) -> None:
        """
        Perform the Monster's first skill, to be implemented in subclasses
        """
        raise NotImplementedError("To be implemented in subclasses")


class Skeleton(Monster):
    """
    A skeleton, subclass of Monster
    """

    def __init__(self) -> None:
        super().__init__(50, 1.2, "Skeleton", 20)
        self.drops = WoodenSword()

    def skill1(self) -> int:
        """
        Skeleton's first skill, a simple slash with it's claws
        Does 10 damage
        """
        print("Skeleton slashes with it's boney claws.")
        return 10



