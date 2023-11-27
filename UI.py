import pygame
from sys import exit
from Player import Player
from Monster import Skeleton


class UI:
    """
    Class representing the User Interface of the game
    Attributes:
        screen
        clock
        over_world
        player_surface
        player_rect
        background_surface
        player
        battle_background
    """
    screen: any
    clock: any
    over_world: bool
    player_surface: any
    player_rect: any
    background_surface: any
    player: Player
    skeleton_rect: any  # FOR NOW KEEP ENEMY AS A ATTRIBUTE, CHANGE THIS LATER
    skeleton_surf: any
    enemy: any
    battle_background: any

    def __init__(self):
        pygame.init()
        # create screen
        self.screen = pygame.display.set_mode((1500, 800))
        pygame.display.set_caption("Game") # Look into changing icon
        self.clock = pygame.time.Clock()  # clock is what affects fps and game speed
        self.over_world = True
        self.player = Player()
        self.enemy = Skeleton()

        # test_font = pygame.font.Font("Pixeltype.ttf", 50)

        self.player_surface = pygame.image.load("human_player_idle.png").convert_alpha()
        self.player_rect = self.player_surface.get_rect(midbottom=(100, 350))

        self.background_surface = pygame.Surface((1500, 800))
        self.background_surface.fill("Brown")

        self.battle_background = pygame.Surface((1500, 800))
        self.battle_background.fill("White")

        self.skeleton_surface = pygame.image.load("snail1.png").convert_alpha()
        self.skeleton_rect = self.skeleton_surface.get_rect(midbottom=(700, 350))

    def run(self):
        #  this while loop is keeping the game running, break from inside
        #  to stop game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if player clicks x on display,
                    pygame.quit()  # close game
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:  # interact button, e
                        pass
                    if event.key == pygame.K_TAB:  # inventory button, tab
                        pass
                    if event.key == pygame.K_m:  # map button, m
                        pass
                    if event.key == pygame.K_ESCAPE:  # menu button, escape
                        pass

                # if event.type == pygame.MOUSEMOTION:  # gives x, y of mouse postion
                #     event.pos
                # if event.type == pygame.MOUSEBUTTONUP:  # if mouse click released
                #     pass

            if self.over_world:
                self.screen.blit(self.background_surface, (0, 0))

                self.screen.blit(self.skeleton_surface, self.skeleton_rect)

                # PLAYER MOVEMENT =============================================
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:  # move up
                    self.player_rect.top -= 5
                if keys[pygame.K_s]:  # move down
                    self.player_rect.bottom += 5
                if keys[pygame.K_d]:  # move right
                    self.player_rect.right += 5
                if keys[pygame.K_a]:  # move left
                    self.player_rect.left -= 5

                self.screen.blit(self.player_surface, self.player_rect)

                # COLLISION =================================================
                if self.skeleton_rect.colliderect(self.player_rect):  # if player collides with enemy, start fight
                    self.over_world = False

                # if player_rect.colliderect(skeleton_rect):  # if player collides with skele
                #     pass  # do something, start battle??

                # mouse_pos = pygame.mouse.get_pos()
                # if player_rect.collidepoint(mouse_pos):
                #     print(pygame.mouse.get_pressed())
            else:  # if battle starts
                self.battle_start(self.player, self.enemy) # call battle start method


            # draw all our elements
            # update everything
            pygame.display.update()
            self.clock.tick(60)  # max fps is 60

    def battle_start(self, player, enemy):
        # while True:
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:  # if player clicks x on display,
            #         pygame.quit()  # close game
            #         exit()
            #     if event.type == pygame.MOUSEBUTTONUP:  # if mouse click released
            #         pass
            # self.screen.blit(self.battle_background, (0, 0))
        player_sprite = pygame.image.load("big_sprite1.png").convert_alpha()
        while self.player.hp >= 0 & enemy.hp >= 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if player clicks x on display,
                    pygame.quit()  # close game
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:  # if mouse click released
                    pass
            self.screen.blit(self.battle_background, (0, 0))
            self.screen.blit(player_sprite, (100, 500))
            # valid_move = True
            # while valid_move:
            #     move = input("Your HP: " + str(player.hp) + "\tYour mana: " +
            #                  str(player.mana) + "\n" + enemy.name + "'s HP: "
            #                  + str(enemy.hp) + "\n" +
            #                  "Enter a move:\n1 (Sword Slash)\n")
            #     if move == "1":
            #         valid_move = False
            #
            #         dmg_done = player.skills[0].perform_move(
            #             player.mana, player.luck, player.damage,
            #             player.weapon1.weapon_dmg)
            #
            #         player.mana -= player.skills[0].mana_usage
            #         if player.mana < 0:
            #             player.mana = 0
            #
            #         print(enemy.name + " takes " + str(
            #             dmg_done) + " points of damage!")
            #         enemy.hp -= dmg_done
            #
            #         if enemy.hp <= 0:  # Monster defeated
            #             print(enemy.name + " was defeated! You win " + str(
            #                 enemy.drops))
            #
            #             print("You gain " + str(enemy.exp_drop)
            #                   + " experience points!")
            #             player.exp += enemy.exp_drop
            #             if player.exp >= player.needed_exp:
            #                 player.lvl_up()
            #
            #             player.bag.append(enemy.drops)
            #             return None
            #     else:
            #         print("Invalid move entered. Try again!")
            # dmg_taken = enemy.skill1()
            # print("You take " + str(dmg_taken) + " points of damage!")
            # player.hp -= dmg_taken
            # if player.hp <= 0:  # Player died
            #     print("You Died!")
            #     return None

            # draw all our elements
            # update everything
            pygame.display.update()
            self.clock.tick(60)  # max fps is 60




# wall = pygame.image.load()  # enter imagine path onto here



