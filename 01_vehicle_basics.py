import carla
import random
import time
import pygame
from pygame.locals import*


vehicle=None

try:
    client=carla.Client("localhost","yourport(default=2000")
    client.set_timeout(10.0)

    world=client.get_world()
    carla_map=world.get_map()

    print("CARLA baglantisi basarili")

    spawn_points=carla_map.get_spawn_points()
    spawn_point=random.choice(spawn_points)

    blueprint_library=world.get_blueprint_library()
    vehicle_bp=blueprint_library.find("vehicle.ford.mustang")

    print("Seçilen araç blueprint:", vehicle_bp.id)

    vehicle=world.try_spawn_actor(vehicle_bp,spawn_point)

    if vehicle is None:
        print("Araç spawn edilemedi")
    else:
        print("Araç spawn edildi")

        pygame.init()
        screen=pygame.display.set_mode((640,480))
        pygame.display.set_caption("CARLA Manuel Surus")

        clock=pygame.time.Clock()
        running=True

        reverse=False
        gear=1

        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.type==K_ESCAPE:
                        running=False
                    if event.key==K_r:
                        gear=-gear
                        reverse=gear==-1
                        if gear==-1:
                            reverse=True
                        else:
                            reverse=False

            keys=pygame.key.get_pressed()
            throttle=0.0
            brake=0.0
            steer=0.0
           

            if keys[K_UP]:
                throttle=1.0
            if keys[K_DOWN]:
                brake=1.0
            if keys[K_LEFT]:
                steer=-0.5
            if keys[K_RIGHT]:
                steer=0.5
               

            control=carla.VehicleControl(
                throttle=throttle,
                brake=brake,
                steer=steer,
                reverse=reverse,
            )

            vehicle.apply_control(control)    

finally:
      if vehicle is not None:
        vehicle.destroy()
      pygame.quit
