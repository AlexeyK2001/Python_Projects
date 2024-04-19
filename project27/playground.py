def add(
    *args,
):  # *args allows to input as many POSITIONAL arguments in function as we want ### ARGS are stored as a TUPLE
    summa = 0
    for i in args:
        summa += i
    return summa


print(add(24, 131, 14, 135151, 15121, 532, 24))


def calculate(n, **kwargs):  # Keyword arguments, stored as a DICTIONARY
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(8, multiply=5, add=3))


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]  ##### CAN BE REPLACED WITH kw.get("make")
        self.model = kw[
            "model"
        ]  ####    IN THIS CASE, THERE WILL BE NO ERROR IF NOTHING IS INPUTED IN ARGUMENTS
        # self.make = kw.get("make")
        # self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(model="Grand Vitara", make="Suzuki", color="black", seats=5)
print(my_car.seats)
