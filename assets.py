import pygame

# Asset pista
background = pygame.image.load('sprites\pista.png')
background_correct_size = pygame.transform.scale(background, (600, 700))

# Asset do carro
car_asset = pygame.image.load('sprites\Car.png')
escala = 0.05
width_adjust = int(car_asset.get_width() * escala)
height_adjust = int(car_asset.get_height() * escala)
car_asset_center = pygame.transform.scale(car_asset, (width_adjust, height_adjust))
car_to_left = pygame.transform.rotate(car_asset_center,11) #asset de movimento para esquerda
car_to_right = pygame.transform.rotate(car_asset_center,-11) #asset de movimento para direita

# Asset zombie
zombie_scale = 0.25
zombie_asset = pygame.image.load('sprites\export_move.gif')
zombie_width_adjust = int(zombie_asset.get_width()* zombie_scale)
zombie_height_adjust = int (zombie_asset.get_height()* zombie_scale)
zombie_asset_adjust = pygame.transform.scale(zombie_asset,(zombie_width_adjust, zombie_height_adjust))
zombie_adjust_rotate = pygame.transform.rotate(zombie_asset_adjust, -90)
