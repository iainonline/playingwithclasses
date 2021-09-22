#create list of objects, methods and attributes

class Object:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        pass

    def createlink(self):
        print('Link created to another object')

    def objectinfo(self):
        print('Object is called ' + self.name + ' and was manufactured in ' + self.year)

    def changeobjectyear(self,year):
        self.year = year
        print('Year changed to ' + year)

ob1 = Object('Playstation 2','1990')
print(ob1)
ob1.objectinfo()
ob1.createlink()
ob1.year = '1991'
ob1.objectinfo()
ob1.changeobjectyear('2020')

objs = list()
for i in range(10):
    objs.append(Object('Default name',str(i)))

objs[0].changeobjectyear('2021')

for i in range(10):
    objs[i].objectinfo()
