import carla
import pygame
import cv2
import time
import random
from pygame import *
from Carla_Baglanti import carla_baglanti
from vehicle_basics import manuel_surus,vehicle_spawn
from RGB_Cameras import rgb_camera_spawn
from weather import get_weather_presets, set_weather

vehicle=None
cameras=[]

client,world,carla_map=carla_baglanti()
spawn_points=carla_map.get_spawn_points()
spawn_point=random.choice(spawn_points)

pygame.init()
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption("CARLA Manuel Surus")
clock=pygame.time.Clock()


def main():
    try:
        vehicle=vehicle_spawn(world,spawn_point)

        if vehicle is None:
            return

        cameras,frame_surfaces=rgb_camera_spawn(world,vehicle)

        running=True
        reverse=False
        gear=1

        weather_presets = get_weather_presets()
        weather_index = 0

        set_weather(
            world,
            weather_presets,
            weather_index
        )

        
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_k:
                        weather_index=(weather_index+1) % len(weather_presets)
                        weather_name=set_weather(
                            world,
                            weather_presets,
                            weather_index
                        )
                        print("Hava Durumu: ",weather_name)
                    if event.key==K_r:
                        gear=-gear
                        reverse=gear==-1
                        if gear==-1:
                            reverse=True
                        else:
                            reverse=False
            camera_positions = {
                "front": (0, 0),
                "rear": (640, 0),
                "left": (0, 360),
                "right": (640, 360)
            }
            camera_labels = {
                "front": "FRONT",
                "rear": "REAR",
                "left": "LEFT",
                "right": "RIGHT"
            }

            font = pygame.font.Font(None, 28)

            for camera_name, position in camera_positions.items():

                frame = frame_surfaces[camera_name]

                if frame is not None:

                    surface = pygame.transform.scale(
                        frame,
                        (640, 360)
                    )

                    screen.blit(surface, position)

                    text_surface = font.render(
                        camera_labels[camera_name],
                        True,
                        (255, 255, 255)
                    )

                    screen.blit(
                        text_surface,
                        (
                            position[0] + 10,
                            position[1] + 10
                        )
                    )

            pygame.display.flip()
            keys=pygame.key.get_pressed()


            manuel_surus(vehicle,keys,reverse)

            clock.tick(60)
       
    finally:
      for camera in cameras:
          camera.stop()
          camera.destroy()
    
      if vehicle is not None:
        vehicle.destroy()


      pygame.quit()

if __name__ == "__main__":
    main()