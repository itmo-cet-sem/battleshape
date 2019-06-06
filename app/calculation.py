import datetime


def remove_outdated_coordinates(coordinates):
    curr = datetime.datetime.utcnow()
    return list(
        filter(lambda x: (curr - x['datetime']).seconds < 10, coordinates))


def calculate_lives(shape):
    return 5


def shoot(whom):
    pass


def killed(who, whom):
    pass
