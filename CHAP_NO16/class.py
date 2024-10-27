class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        
    def moves(self):
        print("moves along...")
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

# my_car = Vehicle("Tesla","Model 3")
# my_car.moves()
# print(my_car.make,my_car.model)
# my_car.get_make_model()

class Airplane(Vehicle):
    def __init__(self,make,model,id):
        super().__init__(make,model)
        self.id = id

    def moves(self):
        print("flies along...")

class Truck(Vehicle):
    def moves(self):
        print("rumbles along...")

class GolfCart(Vehicle):
    pass


emirates = Airplane("Emirates","Model hawk","1")
larri = Truck("Larri","Model 1980")
golfWagon = GolfCart("Yamaha","Model 100")

emirates.moves()
larri.moves()
golfWagon.moves()
emirates.get_make_model()
larri.get_make_model()
golfWagon.get_make_model()
print(
larri.make
)

