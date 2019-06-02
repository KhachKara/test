class Person:
    def __int__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

pl = Person()
pl.firstname = "Khach"
pl.lastname = "Kara"
pl.age = 46
pl.nike = "Boga"
pl.city = "Moscow"
print("{} {} {}".format(pl.firstname, pl.lastname, pl.city))
