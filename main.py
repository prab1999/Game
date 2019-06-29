from game_function import *
from setting import Setting
from pygame.sprite import Group
from information import Info
from button import Button
from pages import *

def run():
    pygame.init()
    pygame.font.init()
    set = Setting()
    screen = pygame.display.set_mode((set.width,set.height))
    info=Info(screen,set)
    pygame.display.set_caption("TicTac")

    blocks=Group()
    winpage=WinPage(screen,set,info)
    pausepage=PausePage(screen,set,info)
    pages={}
    pages['Win']=winpage
    pages['Pause']=pausepage
    pages['Play']=PlayPage(screen,set,info,blocks)
    create_board(screen,set,blocks)
    while True:
        check_event(screen,set,blocks,info,pages)
        update_screen(screen,set,blocks,info,pages)


run()
