import pygame

import pics

class Bird:
    Imgs=pics.Bird_Imgs
    Max_Rotation=25;
    Rot_Vel=20;
    Animation_Time=5;
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
        self.tilt=0;
        self.flips=0;
        self.vel=0;
        self.height=y;
        self.img_count=0;
        self.img=self.Imgs[0];
    def jump(self):
        self.vel=-5.5
        self.flips=0;
        self.height=self.y;
    def move(self):
        self.flips+=1;
        d=self.flips*self.vel+1.5*self.flips**2;
        d=min(d,16);
        if(d<0):
            d-=2;
        self.y+=d;
        if(d<0 or self.y<self.height+50):
            self.tilt=max(self.tilt,self.Max_Rotation);
        elif self.tilt>-90:
            self.tilt-=self.Rot_Vel;


    def draw(self,Window):
        self.img_count+=1;
        x=self.img_count//self.Animation_Time;
        if(x==4):
            x=0;
            self.img_count=0;
        elif(x==3):
            x=1;
        self.img=self.Imgs[x];

        if(self.tilt<=-80):
            self.img=self.Imgs[1];
            self.img_count=self.Animation_Time*2;

        rotated_image=pygame.transform.rotate(self.img,self.tilt);
        new_rect=rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x,self.y)).center);
        Window.blit(rotated_image,new_rect.topleft);

    def get_mask(self):
        return pygame.mask.from_surface(self.img);




