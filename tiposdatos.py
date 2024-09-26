print("Clases v2 Mat:22308051281240")

# Zona de clases 
class Datos:
    # El constructor es una funcion
    def __init__(self, estatura, peso ):
        self.estatura = estatura
        self.peso = peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura}mts, Peso {self.peso}kg")
    def mi_lista(self):
        Flores=[ "girasoles", "tulipanes", "margaritas", "rosas"]
        print(Flores)
        for x in Flores:
            print(x)

    def mi_tupla(self):
        Dulces =("chocolates", "paletas", "bombones")
        for y in Dulces:
            print(y)

    def mi_set(self):
        Prendas = {"tenis", "pantalones", "blusas", "calcetas"}
        for z in Prendas:
            print(z)

    def mi_diccionario(self):
        Playas = { "Clima:" : "Calido", "Interes:": "Turistico", "Ejemplo:": "Playa del Carmen"}
        for a, b in Playas.items():
            print(a,b)

#Creacion de objeto
info=Datos(1.60,70.0)

# Utilizando el objeto --> info
info.mostrar_datos()
print("Lista de info --López Daniela")
info.mi_lista()
print("Lista de Flores-- López Daniela")
info.mi_tupla()
print("Tupla de dulces -- López Daniela ")
info.mi_set()
print("Set de prendas -- López Daniela ")
info.mi_diccionario()
print("Diccionario de playas -- López Daniela ")
