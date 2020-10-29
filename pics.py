import pygame
import os
pygame.font.init()
Bird_Imgs=[];
for i in range(1,4):
    Bird_Imgs.append(pygame.image.load(os.path.join("imgs",f"bird{i}.png")));
Pipe_Img=pygame.image.load(os.path.join("imgs","pipe.png"));
Base_Img=pygame.image.load(os.path.join("imgs","base.png"));
Bg_Img=pygame.image.load(os.path.join("imgs","bg.png"));
Score=pygame.font.SysFont("comicsans",25);