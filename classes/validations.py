class Validations:


    @staticmethod
    def valid_string(string: str):
        if not string:
            raise ValueError("Input cannot be empty!")


    @staticmethod
    def valid_integer(string:str):
        if not string.isdigit():
            raise ValueError("Input must be a whole number!")


    @staticmethod
    def valid_positive(integer:int):
        if integer < 1:
            raise ValueError("Input must be a positive number!")