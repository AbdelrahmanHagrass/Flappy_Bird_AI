import random

import pygame

import pics


class Pipe:
    vel=5
    def __init__(self,x):
        self.x=x;
        self.height=0;
        self.top=0;
        self.gap=100;
        self.bottom=0;
        self.Pipe_Top=pygame.transform.flip(pics.Pipe_Img,False,True);
        self.Pipe_Bottom=pics.Pipe_Img;
        self.passed=False;
        self.set_height();


    def set_height(self):
        self.height=random.randrange(50,300);
        self.top=self.height-self.Pipe_Top.get_height();
        self.bottom=self.height+self.gap;
    def move(self):
        self.x-=self.vel;
    def draw(self,Window):
        Window.blit(self.Pipe_Top,(self.x,self.top));
        Window.blit(self.Pipe_Bottom,(self.x,self.bottom));

    def collide(self,bird):
        bird_mask=bird.get_mask();
        top_mask=pygame.mask.from_surface(self.Pipe_Top);
        bottom_mask=pygame.mask.from_surface(self.Pipe_Bottom);
        top_offset=(self.x-bird.x,self.top-round(bird.y));
        bottom_offset=(self.x-bird.x,self.bottom-round(bird.y));
        bottom_point=bird_mask.overlap(bottom_mask,bottom_offset);
        top_point=bird_mask.overlap(top_mask,top_offset);

        return bool(top_point or bottom_point);

