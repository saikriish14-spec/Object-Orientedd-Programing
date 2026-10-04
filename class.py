class Human:
    species = "homo sapiens"
    def __init__ (self,name,age,ethnicity,languages):
        self.name=name
        self.age=age
        self.ethnicity=ethnicity
        self.languages=languages

bob=Human("Bob", 13, "indian", ["French", "German", "Spanish"])
print(bob.name)
print(bob.age)
print(bob.ethnicity)
print(bob.languages[2])

    