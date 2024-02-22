import pygame, sys, random
from pygame.math import Vector2

class CAR:
    def __init__(self):
        self.car_pos_x = screen.get_width() / 1.9
        self.car_pos_y = 570
        self.position = Vector2(self.car_pos_x, self.car_pos_y)
        self.direction = 0 # 0=meio, 1= direita e -1 = esquerda

    def draw_car(self):
        car_rect = car_asset_center.get_rect(center = (0,0)) #center desenha um rect ao redor de 
        car_rect_left = car_to_left.get_rect(center = (0,0))
        car_rect_right = car_to_right.get_rect(center = (0,0))
        if self.direction == 0:
            screen.blit(car_asset_center,self.position)
        elif self .direction == 1:
            screen.blit(car_to_right,self.position)
        elif self.direction == -1:
            screen.blit(car_to_left,self.position)

# class OBSTACULO:
#     def __init__(self):
#         #create a x and y position
#         self.randomize()

#     def draw_obstaculo(self):
#         #create a rectangle
#         obstaculo_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y*cell_size,cell_size,cell_size)
#         screen.blit(car_asset_adjusted,obstaculo_rect)
#         #draw rectangle
#         #pygame.draw.rect(screen,(126,166,114),fruit_rect)

#     def randomize(self):
#         self.x = random.randint(10,cell_number-8)
#         self.y = random.randint(5,cell_number-8)
#         self.pos = pygame.math.Vector2(self.x, self.y) #vetor de posições

class MAIN():

    def __init__(self):
        self.car = CAR()
        #self.obst = OBSTACULO() 

    def draw_elements(self):
        self.car.draw_car()
        #self.obst.draw_obstaculo()

    def update(self):
        self.check_out()
        self.car.direction = 0
        
    def game_over():
        pygame.quit()
        sys.exit()

    def check_out(self):
        if self.car.position.x < 125 or self.car.position.x > 405:
            pass


#asset pista
background = pygame.image.load('assets\pista.png')
background_correct_size = pygame.transform.scale(background, (600, 700))

#
pygame.init()
screen_height = 700
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meu jogo")
clock = pygame.time.Clock() #para garantir que o jogo não mude de velocidade de pc para pc
#

#makes the movemente in the background
background_yPosition = 0
background_yPosition2 = screen_height

#asset do carro
car_asset = pygame.image.load('assets\y6HviX.png')
escala = 0.05
width_adjustment = int(car_asset.get_width() * escala)
height_adjustment = int(car_asset.get_height() * escala)
car_asset_center = pygame.transform.scale(car_asset, (width_adjustment, height_adjustment))
car_to_left = pygame.transform.rotate(car_asset_center,11)
car_to_right = pygame.transform.rotate(car_asset_center,-11)
#initial pos

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
    if press[pygame.K_LEFT] and main_game.car.position.x > 125:
        main_game.car.direction = -1
        main_game.car.position.x -= 10
    if press[pygame.K_RIGHT] and main_game.car.position.x < 405:
        main_game.car.direction = 1
        main_game.car.position.x += 10 
    if press[pygame.K_UP]:
        main_game.car.position.y -=5
    if press[pygame.K_DOWN]:
        main_game.car.position.y +=5

    background_yPosition += 1
    background_yPosition2 += 1

    if background_yPosition >= screen_height:
        background_yPosition2 = 0
        
    if background_yPosition2 <= -screen_height:
        background_yPosition = screen_height
    
       

    screen.blit(background_correct_size, (0,background_yPosition))
    screen.blit(background_correct_size, (0,background_yPosition2))
    #screen.fill((0,0,0)) #tuple rgb #pode receber pygame.Color('cor')
    main_game.draw_elements()
    #screen.blit(car_asset_adjusted,car_pos) #posição acima a esquerda da surface
    pygame.display.flip()
    clock.tick(60) #garante que o jogo rode a 60 fps
