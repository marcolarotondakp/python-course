from typing_extensions import override


class Vehicle:
    def __init__(self, make, color):
        print("called __init__ from class Vehicle")
        self.make = make
        self.color = color

    def repaint(self, new_color):
        print("Repainting this vehicle...")
        self.color = new_color
        print(f"Now the vehicle is {new_color}!")

    def generic_method(self):
        print("this is a generic method from class Vehicle")

    def drive(self):
        print("I am driving this vehicle")


class Flying:
    def __init__(self, max_height_km) -> None:
        self.max_height_km = max_height_km

    def fly(self):
        print("I am flying")

    def generic_method(self):
        print("this is a generic method from class Flying")


class Helicopter(Flying, Vehicle):
    def __init__(self, make, color, max_height):
        Vehicle.__init__(self, make, color)
        Flying.__init__(self, max_height)

    @override
    def drive(self):
        print("I am driving this helicopter")


if __name__ == "__main__":
    vehicle = Vehicle("ford", "black")
    helicopter = Helicopter("Leonardo", "black", 4000)
    text_multiple_inheritance = f""" In python una classe può ereditare da più classi (multiple inheritance)
Con la definizione della classe Helicopter 
    class Helicopter(Flying, Vehicle):
        ...
stiamo dicento che Helicopter eredita sia da Flying che da Vehicle. In effetti la multiple inheritance serve proprio per modellare
il fatto che un oggetto di tipo A può essere contemporaneamente di più tipi diversi e indipendenti l'uno dall'altro. Nel nostro caso, ogni Helicopter è sia un Vehicle
che un Flying. Poichè Helicopter eredita sia da Vehicle, che da Flying, ha accesso a tutti i campi e metodi definiti nelle rispettive 
classi genitore.
    helicopter.make -> {helicopter.make}
    helicopter.color -> {helicopter.color}
    helicopter.max_height_km -> {helicopter.max_height_km} """
    print(text_multiple_inheritance)

    print("\nEseguo il metodo helicopter.repaint('grey')")
    helicopter.repaint("grey")
    print("\nEseguo il metodo helicopter.fly()")
    helicopter.fly()

    text_method_resolution_order = f"""Un caso a cui prestare attenzione è dato dal metodo generic_method(). Questo method è implementato sia
dalla classe Vehicle, sia da Flying. La classe Helicopter eredita questo metodo, ma da quale delle due classi genitore? Per decidere da quale classe ereditare
il metodo, python calcola un ordine di priorità (il method resolution order). Informalmente, la priorità viene data:
    - prima alla classe target (Helicopter)
    - poi alle classi da cui eredita direttamente, nell'ordine in cui sono dichiarate nella definizione della classe 
    (Flying è prioritaria su Vehicle)
    - infine ai genitori delle classi padre.
Possiamo ispezionare precisamente il method resolution order con il metodo __mro__, che ritorna l'ordinamento tra le classi:
    Helicopter.__mro__ -> {Helicopter.__mro__}
    """
    print(text_method_resolution_order)
    print("Eseguiamo helicopter.generic_method():")
    helicopter.generic_method()

    text_method_resolution_order_example = """Dall'esecuzione del metodo possiamo vedere che Helicopter ha ereditato il methodo generic_method() dalla classe Flying,
perchè la classe Helicopter è definita come
    class Helicopter(Flying, Vehicle):
        ...
Se invece fosse stata definita come
    class Helicopter(Vehicle, Flying):
        ...
allora avrebbe ereditato il metodo generic_method() dalla classe Vehicle.
    """
    print(text_method_resolution_order_example)

    text_method_resolution_order_init = """Osserviamo come il method resolution order influenza il modo di scrivere il metodo __init__ della
classe Helicopter.
    class Helicopter(Flying, Vehicle):
        def __init__(self, make, color, max_height):
            Vehicle.__init__(self, make, color)
            Flying.__init__(self, max_height)
In questo caso non è conveniente usare il metodo super() per accedere ai metodi della classe genitore. Infatti, in virtù del method resolution order,
il metodo super() ci permette di accedere solo ai metodi della classe Flying (la prima classe dichiarata nella definizione di Helicopter).
Per maggiore chiarezza è meglio chiamare i metodi __init__ riferendosi esplicitamente a ciascuna classe genitore.
Nota: è necessario passare il parametro self (ricevuto in input dal metodo __init__ della classe Helicopter) come argomento ai metodi __init__
delle classi Vehicle e Flying.
    """
    print(text_method_resolution_order_init)

    text_override = """Possiamo sfruttare il method resolution order anche per sovrascrivere dei metodi. Per esempio, il metodo drive
della classe Vehicle viene sovrascritto dal metodo drive della classe Helicopter. Il decoratore @override, sebbene non obbligatorio, documenta 
che quel metodo sovrascrive un metodo già presente nella classe genitore. Quindi, mediante la sovrascrittura del metodo, possiamo fornire una
implementazione del metodo specifica per la classe figlia."""
    print(text_override)

    print("Eseguiamo il metodo drive da un oggetto della classe Vehicle:")
    vehicle.drive()
    print("Eseguiamo il metodo drive da un oggetto della classe Helicopter:")
    helicopter.drive()
