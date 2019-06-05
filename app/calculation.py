def remove_outdated_coordinates(coordinates):
    i_oldest = 0
    date_oldest = coordinates[0]['datetime']
    for i in range(1, len(coordinates)):
        if date_oldest < coordinates[i]['datetime']:
            date_oldest = coordinates[i]['datetime']
            i_oldest = i
    del coordinates[i_oldest]


def calculate_lives(shape):
    return 5


def shoot(whom):
    pass


def killed(who, whom):
    pass
