import pygame
import copy
class Info:
    def __init__(self,screen,set):
        self.Title="IT's A TicTac Game"
        self.title_color=(0,0,0)
        self.turn_color=(0,0,0)
        self.player_no="1"
        self.title_x=set.width/2
        self.title_y=set.height/8
        self.title_rect=pygame.Rect(self.title_x,self.title_y,150,60)
        self.turn_rect=copy.copy(self.title_rect)
        self.turn_rect.centery+=80
        self.font_Title=pygame.font.SysFont(None,40)
        self.font_Turn=pygame.font.SysFont(None,25)

        self.screen=screen
        self.game_state="Play"
        self.prep()

    def prep(self):
        self.title_text=self.font_Title.render(self.Title,True,self.title_color)
        self.turn_msg = "Turn : Player " + self.player_no
        self.turn_text=self.font_Turn.render(self.turn_msg,True,self.turn_color)



    def show(self):
        self.screen.blit(self.title_text,self.title_rect)
        self.screen.blit(self.turn_text,self.turn_rect)