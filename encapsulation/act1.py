class myClass:

    __privateVar = 27;

    def _privMeth(self):
        print("I'm inside my class")

    def hello(self):
        print(f"Private variable value: {myClass.__privateVar}")

foo = myClass()
foo.hello()
foo._privMeth()