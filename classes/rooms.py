class Room:


    def __init__(self, name, difficulty, duration, min_players, max_players, price_per_player, is_active=True, room_id="",):
        if not room_id:
            room_id = Room.generate_id()
        self.id = room_id
        self.__name = name
        self.__difficulty = difficulty
        self.duration = duration
        self.min_players = min_players
        self.max_players = max_players
        self.price_per_player = price_per_player
        self.__is_active = is_active
    

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def difficulty(self):
        return self.__difficulty


    @difficulty.setter
    def difficulty(self, difficulty):
        self.__difficulty = difficulty


    @property
    def is_active(self):
        return self.__is_active


    def activate(self):
        self.__is_active = True


    def deactivate(self):
        self.__is_active = False
    

    def is_valid_player(self, players: int)-> bool:
        return self.min_players <= players <= self.max_players


    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(room_dict:dict)-> Room:
        room_id = room_dict["id"]
        name = room_dict["name"]
        difficulty = room_dict["difficulty"]
        duration = room_dict["duration"]
        min_players = room_dict["min_players"]
        max_players = room_dict["max_players"]
        price_per_player = room_dict["price_per_player"]
        is_active = room_dict["is_active"]
        return Room(name, difficulty, duration, min_players, max_players, price_per_player, is_active=is_active, room_id=room_id)


    @classmethod
    def generate_id(objects_list:list):
        last_id = max(map(lambda object: object.id))
        return last_id[0] + f"{(int(last_id[1:]) + 1):03d}"