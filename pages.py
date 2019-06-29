import pygame
from button import Button
import game_function as gf
class WinPage():
    def __init__(self,screen,set,info):
        self.screen=screen
        self.info=info
        self.screen.set_alpha(40)
        self.bg_image=pygame.image.load('bg.jpg').convert(24)
        self.bg_image.set_alpha(30)
        self.image_rect=self.bg_image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.image_rect.center=self.screen_rect.center
        self.restart_but=Button(screen,set,"Restart",48)

        self.winner_msg = "Winner : player"
        self.winner_color = (230, 0, 0)
        self.font_winner = pygame.font.SysFont(None, 50)
        self.winner_rect =pygame.Rect(0,0,80,60)
        self.restart_but_rect=self.restart_but.rect
        self.winner_rect.center=self.restart_but_rect.center
        self.winner_rect.centery-=80

    def prep_winner(self):
        self.winner_msg_copy = self.winner_msg+" "+self.info.player_no
        self.winner_text=self.font_winner.render(self.winner_msg_copy,True,self.winner_color)

    def prep_draw(self):
        self.winner_msg_copy="Draw"
        self.winner_text = self.font_winner.render(self.winner_msg_copy, True, self.winner_color)

    def load(self):
        self.screen.blit(self.bg_image,(0,0))
        self.restart_but.draw()
        self.screen.blit(self.winner_text,self.winner_rect)


class PausePage:
    def __init__(self, screen, set, info):
        self.screen = screen
        self.info = info
        self.screen.set_alpha(40)
        self.bg_image = pygame.image.load('bg.jpg').convert(24)
        self.bg_image.set_alpha(30)
        self.image_rect = self.bg_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.image_rect.center = self.screen_rect.center
        self.resume_but = Button(screen, set, "Resume",48)

    def load(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.resume_but.draw()

class PlayPage:
    def __init__(self,screen,set,info,blocks):
        self.screen=screen
        self.info=info
        self.blocks=blocks
        self.set=set
        self.pause_but=Button(self.screen,self.set,"Pause",30)



    def load(self):
        self.screen.fill(self.set.bg_color)
        self.pause_but.draw()
        gf.show_board(self.screen,self.blocks)
        self.info.show()



