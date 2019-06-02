class Person:
    def __int__(self,
                firstname,
                lastname,
                age,
                city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city

    def calclength(self, arg):
        self.length = len(arg)
        return self.length
pl = Person()
pl.firstname = "Khach"
pl.lastname = "Kara"
pl.age = 46
pl.nike = "Boga"
pl.city = "Moscow"
print("{}".format(pl.calclength(pl.city)))
