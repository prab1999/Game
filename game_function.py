import sys
import pygame
from setting import Setting
from Block import Block

def check_event(screen,set,blocks,info,pages):
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif ev.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_mouse_down(screen,set,blocks,info,mouse_x,mouse_y,pages)

def create_board(screen,set,blocks):
    x=(set.width/2-3*set.block_width)//2
    y=(set.height/2-3*set.block_height)//2
    set.board_x=x
    set.board_y=y
    for i in range(9):
        block=Block(screen,set,x+(i%3)*set.block_width,y+i//3*set.block_height+10)
        blocks.add(block)

def check_mouse_down(screen,set,blocks,info,mouse_x,mouse_y,pages):
    if info.game_state=='Win':
        check_restart(screen,set,blocks,info,mouse_x,mouse_y,pages['Win'].restart_but)

    elif info.game_state=="Pause":
        check_resume(screen, set, blocks, info, mouse_x, mouse_y, pages['Pause'].resume_but)


    elif info.game_state=="Play":

        x1, y1 = set.board_x, set.board_y
        x2, y2 = x1 + set.block_width * 3, y1 + set.block_height * 3

        if (mouse_x >= x1 and mouse_y >= y1) and (mouse_x <= x2 and mouse_y <= y2):
            block_no = ((mouse_x - x1) // set.block_width) + ((mouse_y - y1) // set.block_height) * 3
            click_board(screen, set, blocks,pages, block_no, info)
        else:
            check_pause(screen, set, blocks, info, mouse_x, mouse_y, pages['Play'].pause_but)


def check_restart(screen,set,blocks,info,mouse_x,mouse_y,but):
    if but.rect.collidepoint(mouse_x,mouse_y):
        info.game_state="Play"
        reset_game(screen,set,blocks,info)

def check_pause(screen,set,blocks,info,mouse_x,mouse_y,but):
    if but.rect.collidepoint(mouse_x,mouse_y):
        info.game_state="Pause"

def check_resume(screen,set,blocks,info,mouse_x,mouse_y,but):
    if but.rect.collidepoint(mouse_x,mouse_y):
        info.game_state="Play"


def click_board(screen,set,blocks,pages,block_no,info):
    ch=""
    if info.player_no=="1":
        ch="X"
    else:
        ch="O"

    put_char(screen, set, blocks,info,pages, block_no, ch)

def change_player(info):
    info.player_no=str(3-int(info.player_no))
    info.prep()
def put_char(screen,set,blocks,info,pages,block_no,ch):
    for block in blocks:
        if block.number==block_no:
            if block.value=="":
                block.value=ch
                block.prep()
                block.show()
                if check_winner(screen,set,blocks,info,pages)!=True:
                    Block.fill+=1
                    print(Block.fill)
                    if Block.fill==9:
                        pages['Win'].prep_draw()
                        info.game_state='Win'
                        break
                    change_player(info)

def check_winner(screen,set,blocks,info,pages):
    block_list=list(blocks)
    flag=False
    token=0
    if block_list[0].value!='' and block_list[0].value+block_list[1].value==2*block_list[2].value:
        token=1
    elif block_list[0].value!='' and block_list[0].value+block_list[3].value==2*block_list[6].value:
        token=1
    elif block_list[0].value!='' and block_list[0].value+block_list[4].value==2*block_list[8].value:
        token = 1
    elif block_list[1].value != '' and block_list[1].value + block_list[4].value == 2 * block_list[7].value:
        token = 1
    elif block_list[2].value != '' and block_list[2].value + block_list[5].value == 2 * block_list[8].value:
        token = 1
    elif block_list[2].value != '' and block_list[2].value + block_list[4].value == 2 * block_list[6].value:
        token = 1
    elif block_list[3].value != '' and block_list[3].value + block_list[4].value == 2 * block_list[5].value:
        token = 1
    elif block_list[6].value != '' and block_list[6].value + block_list[7].value == 2 * block_list[8].value:
        token = 1
    if token==1:
        prep_winner_info(screen,set,info,pages)
        return True
    return False


def prep_winner_info(screen,set,info,pages):
    pages['Win'].prep_winner()
    info.game_state="Win"

def update_screen(screen,set,blocks,info,pages):
    if info.game_state=="Win":
        pages['Win'].load()
    elif info.game_state=="Pause":
        pages['Pause'].load()
    elif info.game_state=="Play":
        pages['Play'].load()



    pygame.display.flip()
def reset_game(screen,set,blocks,info):
    for block in blocks:
        block.value=""
        block.prep()
    info.player_no = "1"
    Block.fill=0
    info.prep()

def pause_game(screen,set,play_but):
    screen.fill(set.pause_bg)
    play_but.draw()

def show_board(screen,blocks):
    for block in blocks:
        block.show()
