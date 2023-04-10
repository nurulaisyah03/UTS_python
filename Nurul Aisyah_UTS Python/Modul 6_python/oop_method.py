class marvel:
    def __init__(self,inputname,inputhealth,inputpower,inputarmor) :
        # instance variable
        self.name = inputname 
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor

#void function, method tanpa return
    def siapa(self):
        print("namaku adalah :" + self.name)

    #method dengan argumen
    def healthtambah(self,tambah):
        self.health += tambah

    #method dengan return
    def gethealth(self):
        return self.health
marvel1=marvel('iron man',1000,900,800)
marvel2=marvel("thor",900,1000,900)
marvel3=marvel("iron man",800,700,600)

#pemanggilan method
marvel1.siapa()
#pemakaian method dengan argumen
marvel1.healthtambah(10)
print(marvel1.health)
#mengembalikan nilai dengan method
print(marvel1.gethealth())