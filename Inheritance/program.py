class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm
        

    def show_traits(self):
        print(f"Eye color {self.eye_color}")
        print(f"Height : {self.height_cm}")
        print(f"Ethnicity: {self.ethnicity}")

class Kid(FamilyMember):

    def __init__(self,name,age,eye_color,height_cm, ethnicity):
        self.name = name
        self.eye_color = eye_color
        self.height_cm = height_cm
        self.ethnicity = ethnicity
        
    def show_traits(self):
        print(f"Name :{self.name}")
        print(f"Age: ")
        super().show_traits()

    def favourite_hobby(self, hobby):
        print(self.name, "loves", hobby)


child = Kid("Sai", 13, "Brown", 161, "Indian")

child.show_traits()
child.favourite_hobby("painting")


print("Is kid subclasss of FamilyMember?", issubclass(Kid, FamilyMember))

