class Car(object):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color


car1 = Car('Honda', 'Accord', 'Blue')
car2 = Car(make="Honda", model="Accord", color="blue")
# car1 = Car(, 'Honda', 'Blue')
print(car2.make)
