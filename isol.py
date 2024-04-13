import pygame
from sys import exit
from random import randint
from random import choice,choices

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        snowbear1=pygame.image.load("images/character/snowbear1.png").convert_alpha()
        snowbear1=pygame.transform.scale(snowbear1,(100,70))
        snowbear2=pygame.image.load("images/character/snowbear2.png").convert_alpha()
        snowbear2=pygame.transform.scale(snowbear2,(100,70))
        snowbear3=pygame.image.load("images/character/snowbear3.png").convert_alpha()
        snowbear3=pygame.transform.scale(snowbear3,(100,70))
        snowbear4=pygame.image.load("images/character/snowbear4.png").convert_alpha()
        snowbear4=pygame.transform.scale(snowbear4,(100,70))

        self.snowbearlist=[snowbear1,snowbear2,snowbear3,snowbear4]
        self.snow_index=0

        self.image = self.snowbearlist[self.snow_index]
        self.rect = self.image.get_rect(midbottom = (100,540) )
        self.gravity=0

    def player_input(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.rect.y >=400:
            self.gravity = -17
        if pygame.key.get_pressed()[pygame.K_UP] and self.rect.y >=400:
            self.gravity=-29
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 540:
            self.rect.bottom = 540

    def animation(self):
        self.snow_index += 0.1
        if self.snow_index >= len(self.snowbearlist):
            self.snow_index=0
        self.image=self.snowbearlist[int(self.snow_index)]

    def update(self):
            self.player_input()
            self.apply_gravity()
            self.animation()



class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type=="bat":
            img=pygame.image.load("images/character/bat1.png").convert_alpha()
            img=pygame.transform.scale(img,(50,50))
            x_pos=randint(1100,1800)
            y_pos = choice([250,400,400,400])
        else:
            img=pygame.image.load("images/character/cam.png").convert_alpha()
            img=pygame.transform.scale(img,(100,70))
            x_pos=1200
            y_pos=540

        
        self.image=img
        self.rect=self.image.get_rect(midbottom=(x_pos,y_pos))
    def update(self):
        speed=10
        if self.rect.x>400:
            if int(point/100)>100 and int(point/100)<200:
                speed=15
            if int(point/100)>200 and int(point/100)<400:
                speed=20
            if int(point/100)>400 and int(point/100)<600:
                speed=25
            if int(point/100)>600:
                speed=35
        self.rect.x -= speed
        self.destroy()
    def destroy (self):
        if self.rect.x <= -100:
            self.kill()
    







def score():
    time=pygame.time.get_ticks() - start_time
    score_surf=text.render(f"{int(time/100)}",False,(79,79,79))
    score_rect = score_surf.get_rect(center=(600,100))
    screen.blit(score_surf,score_rect)
    return time

# def obstacle_movement(obstacle_list,speed=10):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             if obstacle_rect.left > randint(400,600):
#                 if int(point/100)>100 and int(point/100)<200:
#                     speed=15
#                 if int(point/100)>200 and int(point/100) <400:
#                     speed=20
#                 if int(point/100)>400:
#                     speed=25
#                     # speed=int(choices([2,30])[0])

#             obstacle_rect.left -=speed
#             if obstacle_rect.bottom==540:
#                 screen.blit(camel,obstacle_rect)
#             else:
#                 screen.blit(bat,obstacle_rect)
            
#         obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-200]
#         return obstacle_list
#     else:
#         return []

def collisions(bear,obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if bear.colliderect(obstacle_rect):
                return False
    return True
        
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle,False):
        obstacle.empty()
        return False
    else: return True

def player_animation():
    global snowbear,snow_index
    snow_index += 0.1
    if snow_index >= len(snowbearlist): snow_index=0
    snowbear=snowbearlist[int(snow_index)]


pygame.init()
pygame.display.set_caption("Isolation")


screen = pygame.display.set_mode((1200,600)) #display surface
clock = pygame.time.Clock()
text=pygame.font.Font("fonts/pixeled/Pixeled.ttf",50)

pygame.init()

game_active=False
start_time=0
point=0
highest_score = 0

#GROUPS
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle=pygame.sprite.Group()


#surfaces
mars_surface = pygame.image.load("images/bg/mars2.png").convert_alpha()
marsnew=pygame.transform.scale(mars_surface,(1200,600))

ground=pygame.image.load("images/bg/ground4.png").convert_alpha()
ground=pygame.transform.scale(ground,(1200,300))

cactus=pygame.image.load("images/bg/cactus.png").convert_alpha()
chhota_cactus=pygame.transform.scale(cactus,(150,100))
bada_cactus=pygame.transform.scale(cactus,(200,150))
bohot_chhota_cactus=pygame.transform.scale(cactus,(70,40))

snowbear1=pygame.image.load("images/character/snowbear1.png").convert_alpha()
snowbear1=pygame.transform.scale(snowbear1,(100,70))
snowbear2=pygame.image.load("images/character/snowbear2.png").convert_alpha()
snowbear2=pygame.transform.scale(snowbear2,(100,70))
snowbear3=pygame.image.load("images/character/snowbear3.png").convert_alpha()
snowbear3=pygame.transform.scale(snowbear3,(100,70))
snowbear4=pygame.image.load("images/character/snowbear4.png").convert_alpha()
snowbear4=pygame.transform.scale(snowbear4,(100,70))

snowbearlist=[snowbear1,snowbear2,snowbear3,snowbear4]
snow_index=0
snowbear=snowbearlist[snow_index]

bear_rect=snowbear.get_rect(midbottom=(100,540))
# bear_gravity=0


# camel=pygame.image.load("images/character/cam.png").convert_alpha()
# camel=pygame.transform.scale(camel,(100,70))

# bat=pygame.image.load("images/character/bat1.png").convert_alpha()
# bat=pygame.transform.scale(bat,(50,50))


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
pygame.time.set_timer(obstacle_timer,900)



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
            obstacle.add(Obstacle(choice(["camel","bat"])))
            # if randint(0,1):
            #     obstacle_rect_list.append(camel.get_rect(midbottom=(randint(1100,1100),540)))
            # else:
            #     obstacle_rect_list.append(bat.get_rect(midbottom=(randint(1100,1800),choices([250,400],[1,3])[0])))



    if game_active:
        screen.blit(marsnew,(0,0))
        screen.blit(ground,(0,540))
        screen.blit(bada_cactus,(800,390))
        screen.blit(bohot_chhota_cactus,(900,300))
        screen.blit(bohot_chhota_cactus,(200,450))
        # screen.blit(score,(score_rect))
        # camel_rect.left-=speed
        # screen.blit(camel,camel_rect)
        point=score()
        screen.blit(chhota_cactus,(900,470))
        screen.blit(bada_cactus,(400,440))
        screen.blit(chhota_cactus,(100,470))

        

        # obstacle_rect_list= obstacle_movement(obstacle_rect_list, speed = 10 )
        # game_active=collisions(bear_rect,obstacle_rect_list)


        # bear_gravity += 1
        # bear_rect.y += bear_gravity
        # if camel_rect.left<-100:
        #     camel_rect.left=1250


        # if bear_rect.bottom >540:
        #     bear_rect.bottom=540

        # player_animation()
        player.draw(screen)
        player.update()
        obstacle.draw(screen)
        obstacle.update()

        # screen.blit(snowbear,bear_rect)


        # if bear_rect.colliderect(camel_rect):
        #     game_active=False
        
        game_active=collision_sprite()

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