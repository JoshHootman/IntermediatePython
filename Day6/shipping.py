import iso6346


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
    def create_with_items(cls, owner_code, *items):
        return cls(owner_code, contents=list(items))

    @staticmethod
    def __make_bic_code(owner_code, serial):
        return iso6346.create(owner_code= owner_code, serial=str(serial).zfill(6))

    def __init__(self, owner_code, contents):
            self.owner_code = owner_code
            self.contents = contents
            # self.next_serial = ShippingContainer.__get_next_serial()
            self.bic = self.__make_bic_code(owner_code=owner_code,
                                                         serial=self.__get_next_serial())


class RefrigeratorShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4

    @staticmethod
    def __make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category='R')

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature is too hot!")
        self.celsius = celsius





























