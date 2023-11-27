# from Player import Player
# from Monster import Skeleton
from UI import UI

if __name__ == '__main__':
    ui = UI()
    ui.run()
    # end_game = True
    # player = Player()
    # while end_game:
    #     valid_input = True
    #     while valid_input:
    #         valid_input = False
    #         command = input("Select one of the following options "
    #                         "with the corresponding number.\n"
    #                         "1: Fight an enemy\n"
    #                         "2: Check bag\n"
    #                         "3: Fully heal!\n"
    #                         "4: Player's stats.\n"
    #                         "5: Stop playing\n")
    #         if command == "5":
    #             end_game = False
    #         elif command == "1":
    #             enemy = Skeleton()
    #             player.fight(enemy)
    #         elif command == "2":
    #             print("Not yet implemented")
    #         elif command == "3":
    #             player.hp = 100
    #             print("You've been fully healed!")
    #         elif command == "4":
    #             print(player.stats())
    #         else:
    #             valid_input = True
    #             print("Invalid input, please try again.")
