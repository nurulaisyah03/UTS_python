#kelas
class Marvel:
    pass

#object
marvel1 = Marvel()
marvel2 = Marvel()
marvel3 = Marvel()

marvel1.name = "Spiderman"
marvel1.health = "1000"

marvel2.name = "Hulk"
marvel2.health = "800"

marvel3.name = "Thor"
marvel3.helath = "900"

#pemanggilan
print(marvel1)
print(marvel1.__dict__)
print(marvel1.name)