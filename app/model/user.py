class User:
    def __init__(self):
        self.x = 0
        self.y = 0
        self._hp = 100
        self.id = 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = (0 if value < 0 else 100 if value > 100 else value)

    def to_dict(self):
        message = {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'hp': self._hp
        }
        return message
