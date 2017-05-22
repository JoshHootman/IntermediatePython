class ShippingContainer:
    next_serial = 1337

    # @staticmethod
    # def __get_next_serial():
    #   result = ShippingContainer.next_serial
    #  ShippingContainer.next_serial += 1
    # return result

    # make it as a class method, not a static
    @classmethod
    def __get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
            self.owner_code = owner_code
            self.contents = contents
            self.next_serial = ShippingContainer.__get_next_serial()

