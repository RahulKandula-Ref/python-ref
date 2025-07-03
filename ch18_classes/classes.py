class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"This is a {self.make}'s {self.model}.")


fam_car = Vehicle('maruti', 'GV')

sr_car = Vehicle('maruti', 'ignis')

print(fam_car.make)
print(sr_car.make)

fam_car.get_make_model()
sr_car.get_make_model()
fam_car.moves()
sr_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa):
        super().__init__(make, model)
        self.faa = faa

    def moves(self):
        print('Files along..')

class GolfCart(Vehicle):
    pass

dream_airplan = Airplane('cessna', 'latest', 'na')
another_d = GolfCart('yamaha', 'ev900')

dream_airplan.get_make_model()
dream_airplan.moves()
another_d.get_make_model()
another_d.moves()


# there is polymorphism above in there as well



