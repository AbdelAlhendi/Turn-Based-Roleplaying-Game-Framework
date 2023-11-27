import random


class Skill:
    """
    Abstract Data Type
    A skill to be used by the Player

    Attributes:
        dmg: the damage multiplier of the skill
        mana_usage: the mana cost to use the skill, if the player does not have
                    enough mana, the skill is still cast but significantly weaker
    """
    dmg: float
    mana_usage: int

    def __init__(self, dmg: float, mana_usage: int) -> None:
        self.dmg = dmg
        self.mana_usage = mana_usage

    def __str__(self) -> str:
        raise NotImplementedError("To be Implemented in a subclass")

    def action_str(self) -> str:
        raise NotImplementedError("To be Implemented in a subclass")

    def perform_move(self, mana: int, luck: int, dmg_multiplier: int,
                     wpn_dmg: int) -> int:
        self.action_str()
        final_dmg = wpn_dmg * self.dmg
        crit_chance = random.randint(0, 10) + luck
        if crit_chance >= 10:
            final_dmg *= 1.5
            print("You get a lucky hit!")

        if mana - self.mana_usage < 0:  # Not enough mana to cast
            print("Your lack of mana weakens your attack.")
            final_dmg *= .2
        return round(final_dmg * (1 + (dmg_multiplier/10)))


class SwordSlash(Skill):
    """
    A simple Sword Slash skill
    """
    def __init__(self) -> None:
        super().__init__(1, 5)

    def __str__(self) -> str:
        return "Sword Slash"

    def action_str(self) -> None:
        print("You swing your sword at your enemy.")

    # def perform_move(self, mana: int, luck: int) -> int:
    #     # print("You swing your sword at your enemy.")
    #     final_dmg = self.dmg
    #     crit_chance = random.randint(0, 10) + luck
    #     if crit_chance >= 10:
    #         final_dmg *= 1.5
    #
    #     return final_dmg
