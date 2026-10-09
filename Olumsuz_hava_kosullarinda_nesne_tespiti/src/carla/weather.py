import carla


def get_weather_presets():

    clear = carla.WeatherParameters.ClearNoon
    cloudy = carla.WeatherParameters.CloudyNoon
    wet = carla.WeatherParameters.WetNoon
    light_rain = carla.WeatherParameters.SoftRainNoon
    medium_rain = carla.WeatherParameters.MidRainyNoon
    heavy_rain = carla.WeatherParameters.HardRainNoon


    fog = carla.WeatherParameters(
        cloudiness=60.0,
        fog_density=45.0,
        fog_distance=20.0,
        wetness=20.0,
        sun_altitude_angle=45.0
    )


    dense_fog = carla.WeatherParameters(
        cloudiness=80.0,
        fog_density=80.0,
        fog_distance=5.0,
        wetness=30.0,
        sun_altitude_angle=30.0
    )


    night = carla.WeatherParameters(
        cloudiness=20.0,
        precipitation=0.0,
        fog_density=0.0,
        wetness=0.0,
        sun_altitude_angle=-30.0
    )

    night_light_rain = carla.WeatherParameters(
    cloudiness=70.0,
    precipitation=25.0,
    precipitation_deposits=20.0,
    wetness=40.0,
    sun_altitude_angle=-20.0
    )

    night_medium_rain = carla.WeatherParameters(
        cloudiness=85.0,
        precipitation=55.0,
        precipitation_deposits=50.0,
        wetness=70.0,
        sun_altitude_angle=-25.0
    )

    night_heavy_rain = carla.WeatherParameters(
        cloudiness=100.0,
        precipitation=90.0,
        precipitation_deposits=80.0,
        wetness=100.0,
        sun_altitude_angle=-30.0
    )

    night_light_fog = carla.WeatherParameters(
    cloudiness=40.0,
    fog_density=20.0,
    fog_distance=40.0,
    sun_altitude_angle=-20.0
    )

    night_medium_fog = carla.WeatherParameters(
        cloudiness=60.0,
        fog_density=50.0,
        fog_distance=20.0,
        sun_altitude_angle=-25.0
    )

    night_dense_fog = carla.WeatherParameters(
        cloudiness=80.0,
        fog_density=80.0,
        fog_distance=5.0,
        sun_altitude_angle=-30.0
    )


    return [
        ("Clear", clear),
        ("Cloudy", cloudy),
        ("Wet", wet),
        ("Light Rain", light_rain),
        ("Medium Rain", medium_rain),
        ("Heavy Rain", heavy_rain),
        ("Fog", fog),
        ("Dense Fog", dense_fog),
        ("Night", night),
        ("Night Light Rain",night_light_rain),
        ("Night Medium Rain",night_medium_rain),
        ("Night Heavy Rain",night_heavy_rain),
        ("Night Light Fog",night_light_fog),
        ("Night Medium Fog",night_medium_fog),
        ("Night Dense Fog",night_dense_fog),


    ]

def set_weather(world, weather_presets, weather_index):

    weather_name, weather = weather_presets[weather_index]

    world.set_weather(weather)

    return weather_name