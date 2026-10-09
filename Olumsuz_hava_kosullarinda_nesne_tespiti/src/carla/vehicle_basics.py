import carla
import random
import time
import pygame
from pygame.locals import*
from Carla_Baglanti import carla_baglanti



def vehicle_spawn(world,spawn_point):

    blueprint_library=world.get_blueprint_library()
    vehicle_bp=blueprint_library.find("vehicle.ford.mustang")
    print("Seçilen araç blueprint:", vehicle_bp.id)
    vehicle=world.try_spawn_actor(vehicle_bp,spawn_point)

    if vehicle is None:
        print("Araç spawn edilemedi")
    else:
        print("Araç spawn edildi")

    return vehicle
    
def manuel_surus(vehicle,keys,reverse):

        velocity=vehicle.get_velocity()

        speed=3.6*(velocity.x**2 + velocity.y**2 + velocity.z**2)** 0.5

        MAX_SPEED=20

        throttle=0.0
        brake=0.0
        steer=0.0
           
        if keys[K_UP]:
            if speed < MAX_SPEED:
             throttle = 1.0
            elif speed > MAX_SPEED + 2:
             brake = 0.2
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
         
