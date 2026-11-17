from datetime import timedelta


class PricingManager:

    
    def calculate_weekend_extra(self, booking_date)-> float:
        if booking_date.strftime("%w") >= "5":
            return 0.15
        return 0.0
        

    def calculate_group_discount(self, players:int)-> float:
        if players >= 7:
            return 0.15
        if players >= 4:
            return 0.1
        else: 
            return 0.0


    def calculate_price(self, room, players, booking_date)-> float:
        base_price = players * room.price_per_player
        after_group_discount = base_price * (1 - PricingManager.calculate_group_discount(players))
        total = after_group_discount * (1 + PricingManager.calculate_weekend_extra(booking_date))
        return total


    def calculate_cancellation_fee(self, booking, current_datetime)-> float:
        if booking.booking_date >= (current_datetime + timedelta(days=1)):
            return 0.0
        if booking.booking_date >= (current_datetime + timedelta(hours=6)):
            return 0.25
        return 0.5
                 