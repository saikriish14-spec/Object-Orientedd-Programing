from abc import ABC, abstractmethod

class Absclass (ABC):

    def print(self,x):
        print("Passed Value : ", x)


    @abstractmethod
    def task(self):
        print("We are insidde the Absclass task")

    def user(self):
        print("Hello my name is Saikriish")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")


test_obj = test_class()
test_obj.task()
test_obj.print(100)
test_obj.user()


