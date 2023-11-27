from Armor import Armor
from Artifact import Artifact
from Item import Item
from Monster import Monster
from Skill import Skill, SwordSlash
from Weapon import Weapon, WoodenSword


class Player:
    """
    The Player that the user controls.
    Attributes:
        hp: the player's health points, if this goes to 0, the player dies
        mana: the player's energy value, used to cast skills
        max_hp: max number of health points of the player
        max_mana: max number of mana points of the player
        weapon1: the player's main weapon, can be None if no weapon equppied
        weapon2: the player's off-hand weapon, can be None if no weapon equppied
        armor: the player's armor, can be None if no armor equppied
        artifact1: the player's first artifact, can be None if no artifact equppied
        artifact2: the player's second artifact, can be None if no artifact equppied
        bag: the player's bag, holds all sorts of items
        skills: a list of the player's skills
        damage: the player's damage stat, influences damage done
        luck: the player's luck stat, influences crit chance and drop chances
        race: the player's race, affects different stats
        exp: the amount of experiance points the player currently has, resets
             to 0 once leveling up
        lvl: the player's current level
        needed_exp: the amount of exp needed to level up, increases with each level
    Representation Invariants:
        hp >= 0
        mana >= 0
        max_hp >= 0
        max_mana >= 0
        damage >= 0
        luck >= 0
        lvl >= 1
        exp >= 0
    """
    hp: int
    mana: int
    max_hp: int
    max_mana: int
    weapon1: Weapon
    weapon2: Weapon
    armor: Armor
    artifact1: Artifact
    artifact2: Artifact
    bag: list[Item]
    skills: list[Skill]
    damage: int
    luck: int
    race: str
    exp: int
    lvl: int
    needed_exp: int

    def __init__(self, race: str = "human") -> None:
        self.hp = 100
        self.mana = 100
        self.max_hp = 100
        self.max_mana = 100
        self.damage = 0
        self.luck = 0
        self.lvl = 1
        self.exp = 0
        self.weapon1 = WoodenSword()
        self.weapon2 = None
        self.armor = None
        self.artifact1 = None
        self.artifact2 = None
        self.bag = []
        self.skills = []
        self.skills.append(SwordSlash())
        self.race = race
        self.needed_exp = 50

    def __str__(self) -> str:
        return "Player"

    def stats(self) -> str:
        return_str = self.race + " player:\n"
        return_str += "HP: " + str(self.hp) + "/" + str(self.max_hp) + "\n"
        return_str += "Mana: " + str(self.mana) + "/" + str(self.max_mana) +\
                      "\n" + "Damage Multiplier: " + str(1 + self.damage/10) + \
                      "\nLuck: " + str(self.luck) + "\nExperience Points: " + \
                      str(self.exp) + "/" + str(self.needed_exp)
        return return_str

    # TODO
    def race_init(self) -> None:
        # Depending on the race, alter the player's stats
        return None

    # TODO test
    def lvl_up(self) -> None:
        valid_input = True
        while valid_input:
            valid_input = False
            lvl_stat1 = input("You've leveled up! Pick two of the following "
                              "stats to increase:\n"
                              "1: Health Points\n2: Mana\n3: Damage\n4: Luck\n")
            lvl_stat2 = input("")
            check = True
            if lvl_stat1 == lvl_stat2:
                print("Invalid input. Try again.")
                check = False
                valid_input = True
            if lvl_stat1 == "1" or lvl_stat2 == "1":
                self.max_hp += 50
                check = False
            if lvl_stat1 == "2" or lvl_stat2 == "2":
                self.max_mana += 30
                check = False
            if lvl_stat1 == "3" or lvl_stat2 == "3":
                self.damage += 1
                check = False
            if lvl_stat1 == "4" or lvl_stat2 == "4":
                self.luck += 1
                check = False
            if check:
                print("Invalid input. Try again.")
                valid_input = True
        self.exp -= self.needed_exp
        self.needed_exp = 50 + (30 * self.lvl - 30)

        if self.exp >= self.needed_exp:
            self.lvl_up()

    def equip_weapon1(self, equipable: Weapon) -> None:
        if equipable.offhand is False:
            equipable.is_mainhand = True
            self.weapon1 = equipable
            self.weapon1.player = self
            print("Equipped " + str(equipable) + ".")
        else:
            print(str(equipable) + " can only be equipped in your offhand.")

    def equip_weapon2(self, equipable: Weapon) -> None:
        self.weapon2 = equipable
        print("Equipped " + str(equipable) + ".")

    def equip_armor(self, equipable: Armor) -> None:
        self.armor = equipable
        print("Equipped " + str(equipable) + ".")

    def equip_artifact1(self, equipable: Artifact) -> None:
        self.artifact1 = equipable
        print("Equipped " + str(equipable) + ".")

    def equip_artifact2(self, equipable: Artifact) -> None:
        self.artifact2 = equipable
        print("Equipped " + str(equipable) + ".")

    def gain_skill(self, new_skill: Skill):
        max_skills = 3
        if self.race == "human":
            max_skills = 4
        if len(self.skills) < max_skills:
            self.skills.append(new_skill)
            print(str(new_skill) + " learned!")
        else:
            print("You've acquired the skill " + str(new_skill))
            valid_input = True
            while valid_input:
                valid_input = False
                print("Max number of skills learned. Choose a skill to"
                      " be replaced by " + str(new_skill) + ".")
                counter = 0
                for i in range(len(self.skills)):
                    print(str(i + 1) + ": " + str(self.skills[i]))
                    counter += 1
                inp = input(
                    str(counter + 1) + ": Do not learn " + str(new_skill))
                replace_ind = -2
                if inp == "1":
                    replace_ind = 0
                elif inp == "2":
                    replace_ind = 1
                elif inp == "3":
                    replace_ind = 2
                elif inp == counter:
                    replace_ind = counter - 1
                elif inp == counter + 1:
                    replace_ind = -1
                else:
                    valid_input = True
                    print("Invalid input, please try again.")

                if replace_ind == -1:
                    print("You did not learn " + str(new_skill) + ".")
                elif replace_ind >= 0:
                    print(str(self.skills[replace_ind]) + " forgotten.")
                    self.skills[replace_ind] = new_skill
                    print(str(self.skills[replace_ind]) + " learned!")

    def fight(self, enemy: Monster) -> None:
        while self.hp >= 0 & enemy.hp >= 0:
            valid_move = True
            while valid_move:
                move = input("Your HP: " + str(self.hp) + "\tYour mana: " +
                             str(self.mana) + "\n" + enemy.name + "'s HP: "
                             + str(enemy.hp) + "\n" +
                             "Enter a move:\n1 (Sword Slash)\n")
                if move == "1":
                    valid_move = False

                    dmg_done = self.skills[0].perform_move(
                        self.mana, self.luck, self.damage,
                        self.weapon1.weapon_dmg)

                    self.mana -= self.skills[0].mana_usage
                    if self.mana < 0:
                        self.mana = 0

                    print(enemy.name + " takes " + str(
                        dmg_done) + " points of damage!")
                    enemy.hp -= dmg_done

                    if enemy.hp <= 0:  # Monster defeated
                        print(enemy.name + " was defeated! You win " + str(
                            enemy.drops))

                        print("You gain " + str(enemy.exp_drop)
                              + " experience points!")
                        self.exp += enemy.exp_drop
                        if self.exp >= self.needed_exp:
                            self.lvl_up()

                        self.bag.append(enemy.drops)
                        return None
                else:
                    print("Invalid move entered. Try again!")
            dmg_taken = enemy.skill1()
            print("You take " + str(dmg_taken) + " points of damage!")
            self.hp -= dmg_taken
            if self.hp <= 0:  # Player died
                print("You Died!")
                return None
