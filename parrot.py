class Parrot:
    species = "bird"

    def __init__(self,name,age):
            self.name = name
            self.age = age



blu = Parrot("Blu", 10)
woo = Parrot("Woo",15)

print(f"Blu is a {blu.species}")
print(f"Woo is a {woo.species}")

print(f"Blu is {blu.age}")
print(f"Woo is {woo.age}")

