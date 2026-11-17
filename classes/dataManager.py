import json
from pathlib import Path
from rooms import Room
from bookings import Booking


class DataManager:
    ROOMS_FILE = Path(__file__).parent.parent / "DB/rooms.json"
    BOOKINGS_FILE = Path(__file__).parent.parent / "DB/bookings.json"


    @classmethod
    def load_rooms(cls)-> list:
        json_content = cls.read_json(cls.ROOMS_FILE)
        return [Room.from_dict(room) for room in json_content]


    @classmethod
    def load_bookings(cls)-> list:
        json_content = cls.read_json(cls.BOOKINGS_FILE)
        return [Booking.from_dict(booking) for booking in json_content]


    @classmethod
    def save_rooms(cls, content:list):
        cls.write_json(cls.ROOMS_FILE)


    @classmethod
    def save_bookings(cls, content: list):
        cls.write_json(cls.BOOKINGS_FILE)


    @staticmethod
    def read_json(path):
        with open(path, "r", encoding="utf-8", newline="\n") as file:
            return json.load(file)


    @staticmethod
    def write_json(path, content):
        json_content = [object.to_dict() for object in content]
        with open(path, "w", encoding="utf-8", newline="\n") as file:
            return json.dump(json_content, file, ensure_ascii=False, indent=4)

