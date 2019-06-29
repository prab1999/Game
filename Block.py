import pygame
from setting import Setting
from pygame.sprite import Sprite
class Block(Sprite):
    count=0
    fill=0
    def __init__(self,screen,set,x,y):
        super(Block,self).__init__()
        self.x=x
        self.value=""
        self.number=Block.count
        self.font=pygame.font.SysFont(None,30)
        self.text_color=(0,0,0)
        self.y=y
        self.color=set.block_color
        self.w=set.block_width
        self.h=set.block_height
        self.screen=screen
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.rect.center=(self.x+self.w,self.y+self.h)
        Block.count+=1
        self.prep()
    def prep(self):
        self.text = self.font.render(self.value, True, self.text_color)

    def show(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.w,self.h),1)

        self.screen.blit(self.text,self.rect)





