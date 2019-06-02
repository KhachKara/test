class Person:
    def __int__(self,
                firstname,
                lastname,
                nikename,
                age,
                city):
        self.firstname = firstname
        self.lastname = lastname
        self.nikename = nikename
        self.age = age
        self.city = city

    def calclength(self, arg):
        self.length = len(arg)
        return self.length
pl = Person()
pl.firstname = "Khach"
pl.lastname = "Kara"
pl.age = 46
pl.nikename = "Boga"
pl.city = "Moscow"
print("{}".format(pl.calclength(pl.city)))
