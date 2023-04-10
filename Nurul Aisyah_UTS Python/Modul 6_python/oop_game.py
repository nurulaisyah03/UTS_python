class marvel:
    def __init__(self,name,health,attackpower,armornumber):
        self.name=name
        self.health=health
        self.attackpower=attackpower
        self.armornumber=armornumber

    def serang(self,lawan):
        print(self.name + " menyerang " + lawan.name )
        lawan.diserang(self,self.attackpower)

    def diserang (self,lawan,attackpower_lawan):
        print (self.name + " diserang " +lawan.name)
        attact_diterima=attackpower_lawan
        print( "serangan terasa : " + str(attact_diterima))
        self.health-=attact_diterima
        print("Darah " + self.name + " tersisa " + str(self.health))

ironman=marvel("iron man",100,10,5)
thor=marvel("thor",95,15,10)

#ironman.serang()
ironman.serang(thor)
#print("\n")
#ironman.serang(thor)
#print("\n")
#thor.serang(ironman)