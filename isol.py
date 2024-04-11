import pygame
from sys import exit
from random import randint
from random import choices

def score():
    time=pygame.time.get_ticks() - start_time
    score_surf=text.render(f"{int(time/100)}",False,(79,79,79))
    score_rect = score_surf.get_rect(center=(600,100))
    screen.blit(score_surf,score_rect)
    return time

def obstacle_movement(obstacle_list,speed=10):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if obstacle_rect.left > randint(400,600):
                if int(point/100)>100 and int(point/100)<200:
                    speed=15
                if int(point/100)>200 and int(point/100) <400:
                    speed=20
                if int(point/100)>400:
                    speed=25
                    # speed=int(choices([2,30])[0])

            obstacle_rect.left -=speed
            if obstacle_rect.bottom==540:
                screen.blit(camel,obstacle_rect)
            else:
                screen.blit(bat,obstacle_rect)
            
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-200]
        return obstacle_list
    else:
        return []

def collisions(bear,obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if bear.colliderect(obstacle_rect):
                return False
    return True
        
pygame.init()
pygame.display.set_caption("Isolation")


screen = pygame.display.set_mode((1200,600)) #display surface
clock = pygame.time.Clock()
text=pygame.font.Font("fonts/pixeled/Pixeled.ttf",50)



game_active=False
start_time=0
point=0
highest_score = 0

#surfaces
mars_surface = pygame.image.load("images/bg/mars2.png").convert_alpha()
marsnew=pygame.transform.scale(mars_surface,(1200,600))

ground=pygame.image.load("images/bg/ground4.png").convert_alpha()
ground=pygame.transform.scale(ground,(1200,300))

cactus=pygame.image.load("images/bg/cactus.png").convert_alpha()
chhota_cactus=pygame.transform.scale(cactus,(150,100))
bada_cactus=pygame.transform.scale(cactus,(200,150))
bohot_chhota_cactus=pygame.transform.scale(cactus,(70,40))

snowbear=pygame.image.load("images/character/snowbear1.png").convert_alpha()
snowbear=pygame.transform.scale(snowbear,(100,70))
bear_rect=snowbear.get_rect(midbottom=(100,540))
bear_gravity=0


camel=pygame.image.load("images/character/cam.png").convert_alpha()
camel=pygame.transform.scale(camel,(100,70))

bat=pygame.image.load("images/character/bat1.png").convert_alpha()
bat=pygame.transform.scale(bat,(50,50))


obstacle_rect_list=[]

gamename=text.render("isoLation",False,'Black')
gamename=pygame.transform.scale(gamename,(600,200))
gamename_rect=gamename.get_rect(center=(600,100))
instruction=text.render("Press  0  to start",False,'White')
instruction=pygame.transform.scale(instruction,(480,50))
instruction_rect=instruction.get_rect(center=(600,400))
instruction1=text.render("Space for jump    and    Up-arrow for high jump",False,'Black')
instruction1=pygame.transform.scale(instruction1,(430,30))
instruction_rect1=instruction1.get_rect(center=(600,500))


#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,600)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and bear_rect.y>=400 :
                    bear_gravity = -20
                if event.key==pygame.K_UP and bear_rect.y>=400 :
                    bear_gravity = -28 
        else:
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_0:
                    game_active=True
                    #camel_rect.left=1200
                    start_time=pygame.time.get_ticks()
        
        if event.type==obstacle_timer and game_active:
            if randint(0,1):
                obstacle_rect_list.append(camel.get_rect(midbottom=(randint(1100,1100),540)))
            else:
                obstacle_rect_list.append(bat.get_rect(midbottom=(randint(1100,1800),choices([250,400],[1,3])[0])))



    if game_active:
        screen.blit(marsnew,(0,0))
        screen.blit(ground,(0,540))
        screen.blit(bada_cactus,(800,390))
        screen.blit(bohot_chhota_cactus,(900,300))
        screen.blit(bohot_chhota_cactus,(200,450))
        # screen.blit(score,(score_rect))
        # camel_rect.left-=speed
        # screen.blit(camel,camel_rect)
        screen.blit(chhota_cactus,(900,470))
        screen.blit(bada_cactus,(400,440))
        screen.blit(chhota_cactus,(100,470))

        point=score()

        obstacle_rect_list= obstacle_movement(obstacle_rect_list, speed = 10 )
        game_active=collisions(bear_rect,obstacle_rect_list)


        bear_gravity += 1
        bear_rect.y += bear_gravity
        # if camel_rect.left<-100:
        #     camel_rect.left=1250


        if bear_rect.bottom >540:
            bear_rect.bottom=540


        screen.blit(snowbear,bear_rect)


        # if bear_rect.colliderect(camel_rect):
        #     game_active=False
        
        

    else:
        screen.fill((71,71,71))
        screen.blit(gamename,gamename_rect)
        screen.blit(instruction,instruction_rect)
        screen.blit(instruction1,instruction_rect1)

        pts=text.render(f"SCORE: {int(point/100)}",False,'Green')
        
        if (int(point/100) >= highest_score and int(point/100) != 0):
            pts3 = text.render("Inshallah High Score Habibi", False, 'Gold')
            pts3=pygame.transform.scale(pts3,(320,35))
            point_rect3=pts3.get_rect(center=(600, 300))
            highest_score = int(point/100)
            screen.blit(pts3,point_rect3)
        pts=pygame.transform.scale(pts,(150,35))
        point_rect=pts.get_rect(center=(600,200))


        
        obstacle_rect_list.clear()

        if int(point/100) !=0:
            screen.blit(pts,point_rect)
            



    pygame.display.update()
    clock.tick(90)