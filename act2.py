# create class

class Vehicle:

    #init method
    color = "blue"
    def __init__(self, max_speed, mileage,price,brand):
         self.max_speed = max_speed
         self.mileage = mileage
         self.price = price
         self.brand = brand
        
modelX = Vehicle(240, 18, 65000, "Mclaren")

print("Model Max Speed:" ,modelX.max_speed)
print("Model Mileage:", modelX.mileage)
print(modelX.color)
print(modelX.price)
print(modelX.brand)