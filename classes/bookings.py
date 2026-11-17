from datetime import date, time, datetime


class Booking:
    def __init__(self, customer_name, room_id, booking_date, start_time, players, total_price, status="Active", cancellation_fee=0.0, booking_id=""):
        self.id = booking_id
        self.customer_name = customer_name
        self.room_id = room_id
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price
        self.status = status
        self.cancellation_fee = cancellation_fee


    @property
    def booking_date(self):
        return self.__booking_date


    @property
    def start_time(self):
        return self.__start_time


    @property
    def players(self):
        return self.players
    



    def cancel_booking(self, fee):
        self.status = "Canclled"
        self.cancellation_fee = fee


    def update_details(self, booking_date, start_time, players, total_price):
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price


    def to_dict(self)-> dict:
        booking_dict = self.__dict__
        booking_dict["booking_date"] = self.__booking_date.strftime("%F")
        booking_dict["start_time"] = self.__start_time.strftime("%R") 
        return booking_dict


    @classmethod
    def from_dict(booking_dict:dict)-> Booking:
        booking_id = booking_dict["id"]
        customer_name = booking_dict["customer_name"]
        room_id = booking_dict["room_id"]
        booking_date = date.strptime(booking_dict["booking_date"], "%F")
        start_time = time.strptime(booking_dict["start_time"], "%R") 
        players = booking_dict["players"]
        total_price = booking_dict["total_price"] 
        status = booking_dict["status"]
        cancellation_fee = booking_dict["cancellation_fee"]
        return Booking(customer_name, room_id, booking_date, start_time, players, total_price, status, cancellation_fee, booking_id)




if __name__ == "__main__":
    test = Booking("Tzvi", "R009", datetime.now().date(), datetime.now().time(), 5, 80.0, booking_id="B010")
    print(test.to_dict())