import pics


class Base:
    vel=5;
    width=pics.Base_Img.get_width();
    Img=pics.Base_Img;
    def __init__(self,y):
        self.y=y;
        self.x1=0;
        self.x2=self.width;

    def move(self):
        self.x1-=self.vel;
        self.x2-=self.vel;
        if(self.x1+self.width<0):
            self.x1=self.x2+self.width;
        if(self.x2+self.width<0):
            self.x2=self.x1+self.width;

    def draw(self,Window):
        Window.blit(self.Img,(self.x1,self.y));
        Window.blit(self.Img,(self.x2,self.y));

