import random
class Instrumento:
    def afinar(self):
        pass
    def tocar(self):
        pass
    def mostrar(self):
        return str(type(self)).split(".")[-1][:-2]
class Piano(Instrumento):
    def tocar(self):
        return "tocando las teclas del piano..."
    def afinar(self):
        return "afinando el piano..."
class Guitarra(Instrumento):
    def tocar(self):
        return"tocando la guitarra..."
    def afinar(self):
        return "afinando la guitarra..."
class Bateria(Instrumento):
    def tocar(self):
        return "tocando la bateria..."
    def afinar(self):
        return "afinando la bateria..."
class Flauta(Instrumento):
    def tocar(self):
        return "tocando la flauta..."
    def afinar(self):
        return "afinando la faluta..."
class Saxofon(Instrumento):
    def tocar(self):
        return "tocando el saxofon..."
    def afinar(self):
        return "afinando el saxofon..."
class Acordeon(Instrumento):
    def tocar(self):
        return "tocando el acordeon..."
    def afinar(self):
        return "afinando el acordeon..."
class Violin(Instrumento):
    def tocar(self):
        return "tocando el violin con el arco..."
    def afinar(self):
        return "afinando el violin..."
class Trombon(Instrumento):
    def tocar(self):
        return "tocando el trombon..."
    def afinar(self):
        return "afinando el trombon..."
class Violonchelo(Instrumento):
    def tocar(self):
        return"tocando el violonchelo..." 
    def afinar(self):
        return"afinando el violonchelo..."
class Trompeta(Instrumento):
    def tocar(self):
        return"tocando la trompeta..."
    def afinar(self):
        return"afinando la trompeta..."
class Musico:
    def __init__(self, nombre):
        self.nombre=nombre
        self.instrumento=None
    def asig_instrumento(self, instrumento):
        self.instrumento=instrumento
    def afinar_instrumento(self):
        return self.instrumento.afinar()
    def tocar_instrumento(self):
        return self.instrumento.tocar()
class Banda:
    def __init__(self):
        self.musicos=[]
        self.instrumentos=[Guitarra(), Piano(), Violin(), Violonchelo(), Saxofon(), Flauta(), Trompeta(), Acordeon(), Bateria(), Trombon()]
        self.amigos=["Juan", "Mafe", "Elian", "Lucho", "Suaza", "Laura", "Matias", "Ruiz", "Isabela", "Diana"]
    def crear_banda(self, cantidad_musicos):
        for i in range(cantidad_musicos):
            self.musicos.append(Musico(random.choice(self.amigos)))
            self.musicos[-1].asig_instrumento(random.choice(self.instrumentos))
    def afinar_banda(self):
        for m in self.musicos:
            print(m.afinar_instrumento())
    def tocar_banda(self):
        for m in self.musicos:
            print(m.tocar_instrumento())
    def mostrar_banda(self):
        for x in self.musicos:
            print(x.nombre)
            print(x.instrumento.mostrar)
if __name__=="__main__":
    b=Banda()
    b.crear_banda(10)
    b.mostrar_banda()
    print("afinamos la banda: ")
    b.afinar_banda()
    print("a tocar: ")
    b.tocar_banda()