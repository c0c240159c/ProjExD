import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img,True,False)
    kouka_img = pg.image.load("fig/3.png")
    kouka_img = pg.transform.flip(kouka_img,True,False)
    kouka_lct = kouka_img.get_rect()
    kouka_lct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # bg_lct = bg_img.get_rect()
        # bg_flip_lct = bg_img.get_rect()
        # bg_lct.center = 800-tmr,400
        # bg_flip_lct.center = 2400-tmr,400
        # screen.blit(bg_img, bg_lct)
        # screen.blit(bg_img,bg_flip_lct)
        x = tmr
        leng = 0
        wid = 0
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img_flip,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        screen.blit(kouka_img,kouka_lct)
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            wid = -1
        if key_lst[pg.K_DOWN]:
            wid = 1
        if key_lst[pg.K_LEFT]:
            leng = -1
        if key_lst[pg.K_RIGHT]:
            leng = 2
        kouka_lct.move_ip(-1+leng,0+wid)
        pg.display.update()
        tmr += 1
        if tmr == 3199:
            tmr = 0   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()