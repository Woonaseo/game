import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE =  pygame.display.set_mode((400,200))
FPSCLOCK = pygame.time.Clock()

def main():
    sysfont = pygame.font.SysFont(None,72)#폰트명(기본으로 지정할때는 None),폰트크기,bold,italic(이태릭인지 아닌지)
    message = sysfont.render("Hello Python",True,(0,128,128))#그리는 텍스트,안티앨리언스,색,배경색(스킵)
    message_rect = message.get_rect()

    while True :
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((225,225,225))
        SURFACE.blit(message,message_rect)
        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == "__main__":
    main()
