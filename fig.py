class kubs:
    def __init__(self,mala,krasa):
        if mala>=2 and mala<=10:
            self.mala=mala
        else:
            print("Neatbilstošs malas garums!!!")
            self.mala=4
        self.krasa=krasa

    def aprekinat_tilpumu(self):
        tilp=self.mala**3
        return int(tilp)

    def __del__(self):#izdzēš objektu
        print("Objekts ir likvidēts. Krāsa: ",self.krasa)

    
#objekti 
kubg=kubs(10,"zaļa")
kubr=kubs(1,"sarkana")
        
print("Kuba g tilpums: ",kubg.aprekinat_tilpumu()," Krāsa ",kubg.krasa)
print("Kuba r malas garums",kubr.mala)
#objekt dzēšana
del kubr
try: 
    print(kubr.mala)
except:
    print("Objekts neeksistē!!!")

print("Kuba g malas garums", kubg.mala)

class bloks(kubs):
    def __init__(self,mala,krasa,kubu_skaits,formas):
        super().__init__(mala,krasa)
        if kubu_skaits>=1 and kubu_skaits <= 4:
            self.__kubu_skaits=kubu_skaits
        else:
            print("Neatbilstoša kubu skaita vērtība!!!")
        self.nosaukums=str(self.krasa)+str(kubu_skaits)
        formas_vertibas = [11,12,13,14,22]
        if formas not in formas_vertibas:
            print("Neatbilst nosacījumiem!!!")
            self.derigums = 0
        else:
            self.derigums = 1


    def tilpums(self):
        kuba_tilpums=self.mala**3
        bloka_tilpums=kuba_tilpums*self.__kubu_skaits
        return bloka_tilpums

    def mainit_formu(self,jauna_forma):
        formas_vertibas = [11,12,13,14,22]
        if jauna_forma not in formas_vertibas:
            print("Neatbilst nosacījumiem!!!")
            self.derigums = 0
        else:
            self.derigums = 1


#objektI
orange3=bloks(5,"oranža",3,13)
print(orange3.nosaukums,orange3.tilpums())
blue5=bloks(7,"ZILS",5,23)
print(blue5.nosaukums,blue5.derigums)
blue5.mainit_formu(12)
print(blue5.nosaukums,blue5.derigums)