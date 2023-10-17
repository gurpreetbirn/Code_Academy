"""A class must be instantiated.In other words, we must create an instance of the class, in order to breathe life into
 the schematic."""


class Facade:
    pass


# instantiating a class
# facade_1 would be known as an object
facade_1 = Facade()


facade_1_type = type(facade_1)
print(facade_1_type)