class Abc:

    x = 10        # public
    _x1 = 15      # protected
    __x2 = 20     # private

    def __init__(self, fname, lname):
        print("Constructor2 called")
        self.fname = fname
        self.lname = lname        

    def __display(self):
        print(self.__x2)
        print(self.fname + " " + self.lname)

class Xyz(Abc):
    def __init__(self, fname, lname, fname1):
        super().__init__(fname, lname, )
        self.fname = fname1

    def display(self):
        print(self._x1)
        print(self.fname)

obj = Xyz("Pankaj", "Kapoor", "Kumar")
obj1 = Abc("Pankaj", "Kapoor")
obj.display()
obj1.display()
print(obj.fname)
