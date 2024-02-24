import pygame, sys, random
from pygame.math import Vector2
import assets

class backgorund:
    def __init__(self) -> None:
        pass

class CAR:
    def __init__(self):
        self.car_pos_x = screen.get_width() / 1.9
        self.car_pos_y = 570
        self.position = Vector2(self.car_pos_x, self.car_pos_y)
        self.direction = 0 # 0=meio, 1= direita e -1 = esquerda

    def draw_car(self):
        car_rect = assets.car_asset_center.get_rect(center = (0,0)) #center desenha um rect ao redor de 
        car_rect_left = assets.car_to_left.get_rect(center = (0,0))
        car_rect_right = assets.car_to_right.get_rect(center = (0,0))
        if self.direction == 0:
            screen.blit(assets.car_asset_center,self.position)
        elif self .direction == 1:
            screen.blit(assets.car_to_right,self.position)
        elif self.direction == -1:
            screen.blit(assets.car_to_left,self.position)
    #def shoot_car:
        

class OBSTACULO:
    def __init__(self):
        #create a x and y position
        self.randomize()
        self.draw_obstaculo()

    def draw_obstaculo(self):
        #create a rectangle
        #self.randomize()
        zombie_rect = assets.zombie_asset.get_rect(center = (0,0))
        screen.blit(assets.zombie_adjust_rotate, self.pos)

    def randomize(self):
        self.x = random.randint(125,405)
        self.y = random.randint(0,450)
        self.pos = pygame.math.Vector2(self.x, self.y) #vetor de posições

    def move_obstaculo(self):
        self.pos.y += 4
    

class MAIN():

    def __init__(self):
        self.car = CAR()
        self.obst = OBSTACULO() 

    def draw_elements(self):
        self.car.draw_car()
        self.obst.draw_obstaculo()

    def update(self):
        self.check_out()
        self.car.direction = 0
        #self.obst.draw_obstaculo()
        self.obst.move_obstaculo()
        
    def game_over():
        pygame.quit()
        sys.exit()

    def check_out(self):
        if self.car.position.x < 130 or self.car.position.x > 405:
            pass


pygame.init()
screen_height = 700
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meu jogo")
clock = pygame.time.Clock() # para garantir que o jogo não mude de velocidade de pc para pc



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True: # loop game
    # desenhar todos o elmentos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.game_over() #garante que vai fechar o jogo
        if event.type == SCREEN_UPDATE:
            main_game.update()
    
    press = pygame.key.get_pressed()
    if press[pygame.K_LEFT] and main_game.car.position.x > 130:
        main_game.car.direction = -1
        main_game.car.position.x -= 10
    if press[pygame.K_RIGHT] and main_game.car.position.x < 407:
        main_game.car.direction = 1
        main_game.car.position.x += 10 
    if press[pygame.K_UP]:
        main_game.car.position.y -=5
    if press[pygame.K_DOWN]:
        main_game.car.position.y +=5

    screen.blit(assets.background_correct_size, (0,0))
    

    main_game.draw_elements()
    pygame.display.flip()
    clock.tick(60) # garante que o jogo rode a 60 fps
