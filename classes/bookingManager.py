from bookings import Booking 
from pricingManager import PricingManager
from .utils import Utils


class BookingManager:

    def __init__(self, rooms: list, bookings: list):
        self.rooms = rooms
        self.bookings = bookings
        self.pricing_manager = PricingManager()

    
    def create_booking(self, customer_name, room_id, booking_date, start_time, players) -> tuple:
        room = Utils.item_by_ID(room_id, self.rooms)
        total_price = self.pricing_manager.calculate_price(room, players, booking_date)
        return "success", "New booking created", Booking(customer_name, room_id, booking_date, start_time, players, total_price)


    def get_booking(self, booking_id)-> Booking:
        return Utils.item_by_ID(booking_id, self.bookings)


    def get_customer_bookings(self, customer_name: str)-> list:
        return Utils.search_by_value("customer_name", customer_name, self.bookings, partial=True)


    def get_bookings_by_date(self, booking_date)-> list:
        return Utils.search_by_value("booking_date", booking_date, self.bookings)


    def check_availability(self, room_id, booking_date, start_time, exclude_booking_id=None)
        