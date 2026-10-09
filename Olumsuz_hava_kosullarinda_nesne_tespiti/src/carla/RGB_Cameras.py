import carla
import numpy as np
import pygame


def rgb_camera_spawn(world, vehicle):

    blueprint_library = world.get_blueprint_library()
    camera_bp = blueprint_library.find("sensor.camera.rgb")

    camera_bp.set_attribute("image_size_x", "640")
    camera_bp.set_attribute("image_size_y", "480")
    camera_bp.set_attribute("fov", "90")

    front_transform = carla.Transform(
        carla.Location(x=1.5, y=0.0, z=1.8),
        carla.Rotation(yaw=0)
    )

    rear_transform = carla.Transform(
        carla.Location(x=-1.5, y=0.0, z=1.8),
        carla.Rotation(yaw=180)
    )

    left_transform = carla.Transform(
        carla.Location(x=0.0, y=-0.9, z=1.8),
        carla.Rotation(yaw=-90)
    )

    right_transform = carla.Transform(
        carla.Location(x=0.0, y=0.9, z=1.8),
        carla.Rotation(yaw=90)
    )

    camera_transforms = [
        ("front", front_transform),
        ("rear", rear_transform),
        ("left", left_transform),
        ("right", right_transform)
    ]

    cameras = []

    # Her kameranın son görüntüsünü burada tutacağız
    frame_surfaces = {
        "front": None,
        "rear": None,
        "left": None,
        "right": None
    }

    def process_image(image, camera_name):

        array = np.frombuffer(image.raw_data, dtype=np.uint8)
        array = array.reshape((image.height, image.width, 4))
        array = array[:, :, :3]
        array = array[:, :, ::-1]

        surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))

        frame_surfaces[camera_name] = surface

    for camera_name, camera_transform in camera_transforms:

        camera = world.spawn_actor(
            camera_bp,
            camera_transform,
            attach_to=vehicle
        )

        camera.listen(
            lambda image, name=camera_name: process_image(image, name)
        )

        cameras.append(camera)

    return cameras, frame_surfaces