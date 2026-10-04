class Parrot:
    species = "bird"
    

    def __init__(self,name,age,wing_color):
            self.name = name
            self.age = age
            self.wing_color = wing_color


blu = Parrot("Blu", 10,"Blue")
woo = Parrot("Woo",15, "Yellow")

print(f"Blu is a {blu.species}")
print(f"Woo is a {woo.species}")

print(f"Blu is {blu.age}")
print(f"Woo is {woo.age}")
print(f"Blu's wing color is {blu.wing_color}")
print(f"Woo's wing color is {woo.wing_color}")


