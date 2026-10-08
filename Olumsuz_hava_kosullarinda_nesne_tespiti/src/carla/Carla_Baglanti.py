import carla


def carla_baglanti():
    client=carla.Client("localhost",2000)
    client.set_timeout(10.0)

    world=client.get_world()
    carla_map=world.get_map()

    print("CARLA baglantisi basarili")

    return client,world,carla_map