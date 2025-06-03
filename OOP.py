# ###Před OOP###
# #seznam
# zamestnanec_01 = ["Karel Dvořák", "instalatér", 25]
# zamestnanec_02 = ["Jana Pokorná", "prodavačka", 25]

# #slovník
# zamestnanec_01 = {"jmeno": "Karel Dvořák", "pozice" : "instalatér", "dni_dovolene": 25}
# zamestnanec_02 = {"jmeno": "Jana Pokorná", "pozice" : "prodavačka", "dni_dovolene": 25}

# #čerpání dovolené zaměstnance 01 - 10 dní
# zamestnanec_01["dni_dovolene"] = zamestnanec_01["dni_dovolene"] - 10

# #kontrola, jestli nedochází k přečerpání dovolené
# pozadovane_dny_dovolene = 10
# if pozadovane_dny_dovolene > zamestnanec_01["dni_dovolene"]:
#     zamestnanec_01["dni_dovolene"] = zamestnanec_01["dni_dovolene"] - pozadovane_dny_dovolene
#     print("Dovolená schválena.")
# else:
#     print("Nedostačené množství dní dovolené. Dovolenou nelze čerpat.")

# #funkce
# def zadost_o_dovolenou(pozadovane_dny_dovolene):
#     if pozadovane_dny_dovolene > zamestnanec_01["dni_dovolene"]:
#         zamestnanec_01["dni_dovolene"] = zamestnanec_01["dni_dovolene"] - pozadovane_dny_dovolene
#         print("Dovolená schválena.")
#     else:
#         print("Nedostačené množství dní dovolené. Dovolenou nelze čerpat.")

# zamestnanec_01 = {"jmeno": "Karel Dvořák", "pozice" : "instalatér", "dni_dovolene": 25}
# zadost_o_dovolenou(10)

###objekty a třídy###

##třída##
class Employee: #název třídy s velkým písmenem
    #tato třída slouží k vytváření objektů, které reprezentují zaměstnace se  3 údaji (jméno, pracovní pozice a počet dnů dovolené)
    def __init__(self, name, position, holiday_entitlement): 
        #__init__ tato metoda se spouští automaticky, když je vytvořen nový objekt třídy
        #self - odkazuje na konkrétní objekt, který se právě vytváří
        #zbylé jsou parametry
        self.name = name
        #self.name - přiřadí hodnotu z parametru name do vlastnosti (atributu) objektu self.name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def get_info(self): #metoda get_info vypisuje informace o zaměstnanci
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    # def __str__(self): #metoda get_info vypisuje informace o zaměstnanci
    #     return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
        #místo get_info se dá použít __str__, pak bude fungovat print(hruby_k)
    
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Máte nárok na dovolenou."
        else:
            return f"Bohužel, už máte nárok pouze na {self.holiday_entitlement} dní."
#print se nedá dát bezprostředně po class, ale až po vytvoření objektů ("naplnění formuláře class informacemi objekt")        

    
##objekt##
#vytvoření zaměstnanců s informacemi o nich
hruby_k = Employee("Karel Hrubý", "instalatér", 25)
vesela_i = Employee("Ivana Veselá", "prodavačka", 25)

#zavolání metody get_info
print(hruby_k.get_info())
print(vesela_i.get_info())

#zavolání metody take_holiday
print(hruby_k.take_holiday(5))
print(hruby_k.take_holiday(30))
print(hruby_k) #nebude fungovat, pokusí se převést objekt na typ řetězec


#vytvoření třídy Package  
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self): #v závorce musí být self
        return f"Balík na adresu {self.address} má hmotnost {self.weight} a je ve stavu {self.state}."
    
    def delivery_price(self):
        if self.weight < 10:
            return 129 #musí být return
        elif self.weight > 10 and self.weight < 20: #and s malým písmenem
            return 159
        else:
            return 359
    def deliver(self):
        #zjistí, jestli byl balíček doručen
        if self.state == "doručen": #pokud state = doručen, pak vypíše větu
            return "Balík už byl doručen."
        else:
            self.state = "doručen" #pokud state je jiný, tak se state změní na doručen
            return "Doručení uloženo." #vypíše se věta
    
pg001 = Package("Báňská 239, Ostrava", 0.153, "doručen") #objekt mimo třídu, tzn. neodsazen
pg002 = Package("Vodní 3, Přerov", 21.12, "nedoručen")
pg003 = Package("Žárová 1289, Hulín", 125.4, "nedoručen")

print(pg001.get_info())
print(pg002.get_info())

print(f"Cena za doručení je {pg002.delivery_price()}.")

print(pg002.deliver()) #ověření stavu doručení balíku, resp. ověření a změna na doručen
# při druhém zavolání už hlásí dřívější doručení
print(pg002.get_info()) #ověření, že deliver zafungoval
