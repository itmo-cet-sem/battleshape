class User:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.__hp = 100
        self.id = 0

    def set_hp(self, hp):
        self.__hp = (0 if hp < 0 else 100 if hp > 100 else hp)

    def to_json(self):
        message = {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'hp': self.__hp
        }
        return message
