from validations import Validations

class Inputs:


    @staticmethod
    def valid_input(input_messege:str, validation_trigger:function):
        is_valid = False
        while not is_valid:
            try:
                user_input = input(input_messege)
                validation_trigger(user_input)
                is_valid = True
            except ValueError as error:
                print(f"Error: {error}")
        return user_input


    @staticmethod
    def get_string(messege: str)-> str:
        return Inputs.valid_input(messege, Validations.valid_string)


    @staticmethod
    def get_integer(messege: str)-> int:
        return int(Inputs.valid_input(messege, Validations.valid_integer))


