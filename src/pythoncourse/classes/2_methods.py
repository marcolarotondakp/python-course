class Vehicle:
    def __init__(self, make, color):
        self.make = make
        self.color = color

    def repaint(self, new_color):
        print("Repainting the car...")
        self.color = new_color
        print(f"Now the car is {new_color}!")

    @classmethod
    def from_list(cls, lista):
        """
        Input: una lista di stringhe. Il primo elemento è la marca, il secondo
        è il colore.
        Output: una nuova istanza della classe Vehicle.
        """
        return cls(lista[0], lista[1])

    @staticmethod
    def miles_to_km(miles):
        return miles * 1.6


if __name__ == "__main__":
    text_instance_methods = """I metodi definiti all'interno di una classe sono di default instance methods.
Per esempio, repaint è un instance method. Se vogliamo definire un tipo diverso di metodo, allora possiamo
annotare i metodi con i decoratori @classmethod e @staticmethod.
    """
    print(text_instance_methods)

    black_ford = Vehicle.from_list(["ford", "black"])
    text_classmethod = f"""A differenza degli instance methods, i class methods non operano su un'istanza della classe,
ma sulla classe stessa. Il primo parametro di un class method non è self (un'istanza), ma cls (la classe, ovvero Vehicle)
Possiamo quindi chiamare un classmethod nel seguente modo:
    black_ford = Vehicle.from_list(["ford", "black"]) -> {black_ford}
Come nel caso degli instance methods, quando viene chiamato un class method con la dot notation, python è in grado di sostituire
il parametro cls con Vehicle.
Quindi l'istruzione
    return cls(lista[0], lista[1])
è equivalente a
    return Vehicle(lista[0], lista[1])
"""
    print(text_classmethod)

    km = Vehicle.miles_to_km(10)
    text_staticmethod = f"""Un ultimo tipo di metodo che possiamo definire all'interno di una classe è dato dagli staticmethod.
In questo caso quello che dobbiamo fare è annotare un metodo con il decoratore @statichmethod.
Un metodo statico non ha 'parametri extra' come self o cls. Si comporta esattamente come una normale funzione, ma per chiamare un metodo statico
dobbiamo farlo a partire dalla classe corrispondente:
    Vehicle.miles_to_km(10) -> {km}
Ha senso usare static method al posto di semplici funzioni nel caso in cui abbiamo una funzione di cui siamo molto sicuri che verrà usata
solo nel contesto della classe. Per esempio, se nella nostra applicazione la conversione da miglia a km viene utilizzata esclusivamente per 
manipolare i dati del tachimetro, allora può essere una scelta sensata implementarla come metodo statico della classe Vehicle.
Viceversa, se dovesse essere usata anche per (e.g.) manipolare misure di campi coltivati, allora è una scelta migliore fare un modulo indipendente
che contenga la funzione.
"""
    print(text_staticmethod)

    text_best_practice = f"""Class methods e static methods possono essere chiamati anche da istanze della classe:
    black_ford.miles_to_km(100) -> {black_ford.miles_to_km(100)}
    black_ford.from_list(["lancia", "white"]) -> {black_ford.from_list(["lancia", "white"])}
Tuttavia, questa non è una pratica generalmente da evitare, perchè potrebbe creare confusione per chi legge il codice e indurlo a pensare che questi
siano instance methods.
    """
    print(text_best_practice)
