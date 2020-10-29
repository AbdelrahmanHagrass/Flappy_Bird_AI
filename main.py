import pygame
import neat
import time
import os
import random
import pics
from Base import Base
from Bird import Bird
from Pipe import Pipe
pygame.font.init()
width=290;
height=500;

def draw_window(Window,birds,pipes,base,score):
    Window.blit(pics.Bg_Img,(0,0))
    text=pics.Score.render(f"Score: {score}",1,(255,255,255));
    Window.blit(text,(width-10-text.get_width(),10))
    for pipe in pipes:
        pipe.draw(Window);
    base.draw(Window)
    for bird in birds:
        bird.draw(Window);
    pygame.display.update()
def main(genomes,config):
    nets=[];
    ge=[];
    birds=[];
    for _,g in genomes:
        net=neat.nn.FeedForwardNetwork.create(g,config);
        nets.append(net);
        birds.append(Bird(100,200));
        g.fitness=0;
        ge.append(g);

    base=Base(400);
    pipes=[Pipe(500)];
    run=True;
    score=0;
    clock=pygame.time.Clock();
    Window=pygame.display.set_mode((width,height));
    while(run):
        clock.tick(30);
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False;
                pygame.quit();
                quit();
        pipe_idx=0;
        if(len(birds)>0):
            if(len(pipes)>1 and birds[0].x>pipes[0].x+pipes[0].Pipe_Top.get_width()):
                pipe_idx=1;
        else:
            run=False
            break;
        for x,bird in enumerate(birds):
            bird.move();
            ge[x].fitness+=0.1;
            output=nets[x].activate((bird.y,abs(bird.y-pipes[pipe_idx].height),
                                     abs(bird.y-pipes[pipe_idx].bottom)));
            if(output[0]>0.5):
                bird.jump();
        remove=[];
        add_pipe=False
        b_remove=[];
        for pipe in pipes:
            for x, bird in enumerate(birds):
              if(pipe.collide(bird)):
                 ge[x].fitness-=1;
                 birds.pop(x);
                 ge.pop(x);
                 nets.pop(x);

              if (not pipe.passed and pipe.x < bird.x):
                  pipe.passed = True;
                  add_pipe = True;
            if(pipe.x+pipe.Pipe_Top.get_width()<0):
                remove.append(pipe);

            pipe.move();
        if(add_pipe):
            score+=1
            for g in ge:
                g.fitness+=5;
            pipes.append(Pipe(500));
        base.move()
        for p in remove:
            pipes.remove(p);
        for x,bird in enumerate(birds):
            if(bird.y+bird.img.get_height()>=400 or bird.y<0):
                birds.pop(x);
                ge.pop(x);
                nets.pop(x);

        draw_window(Window,birds,pipes,base,score);


def run(config_path):
    config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet
                              ,neat.DefaultStagnation,config_path);
    p=neat.Population(config);
    p.add_reporter(neat.StdOutReporter(True));
    stats=neat.StatisticsReporter();
    p.add_reporter(stats);
    winner=p.run(main,50);
if __name__=="__main__":
    Local_Dir=os.path.dirname(__file__);
    config_path=os.path.join(Local_Dir,"CONFIG.txt");
    run(config_path);