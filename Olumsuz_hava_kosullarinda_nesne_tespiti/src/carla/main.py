import carla
import pygame
import cv2
import time
import random
from pygame import *
from Carla_Baglanti import carla_baglanti
from vehicle_basics import manuel_surus,vehicle_spawn

try:
    vehicle=None

    client,world,carla_map=carla_baglanti()
    spawn_points=carla_map.get_spawn_points()
    spawn_point=random.choice(spawn_points)

    pygame.init()
    screen=pygame.display.set_mode((640,480))
    pygame.display.set_caption("CARLA Manuel Surus")
    clock=pygame.time.Clock()


    def main():

        vehicle=vehicle_spawn(world,spawn_point)
        manuel_surus(vehicle,clock)


    main()

finally:
      if vehicle is not None:
        vehicle.destroy()
      pygame.quit()
