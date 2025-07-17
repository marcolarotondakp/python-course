class Vehicle:
    def __init__(self, make, color):
        print("called __init__ from class Vehicle")
        self.make = make
        self.color = color

    def repaint(self, new_color):
        print("Repainting this vehicle...")
        self.color = new_color
        print(f"Now the vehicle is {new_color}!")


class Car(Vehicle):
    def __init__(self, make, color, body_type):
        super().__init__(make, color)
        self.body_type = body_type


class Motorcycle(Vehicle):
    def __init__(self, make, color, has_sidecar):
        super().__init__(make, color)
        self.has_sidecar = has_sidecar


if __name__ == "__main__":
    black_ford = Car("ford", "black", "hatchback")
    bmw_motorcycle = Motorcycle("bmw", "blue", False)
    car_is_vehicle = isinstance(black_ford, Vehicle)
    motorcycle_is_vehicle = isinstance(bmw_motorcycle, Vehicle)
    text_inheritance = f"""
Le classi possono modellare la relazione is_a  tramite il meccanismo di inheritance
(ereditarietà). Noi sappiamo che le automobili sono veicoli, e che le moto sono veicoli, quindi vogliamo che le
classi che abbiamo definito riflettano questa proprietà reale. Per fare in modo che una classe A erediti da una classe B
bisogna usare la seguente sintassi:
    class A(B)
        ...
Nel nostro caso:
    class Car(Vehicle)
        ...
    class Motorcycle(Vehicle)
        ...
quindi sia la classe Car che la classe Motorcycle ereditano dalla classe Vehicle. Questo significa che ogni istanza della classe
Car (o Motorcycle) è anche un'istanza della classe Vehicle.
Creiamo un oggetto Car e un oggetto Motorcycle:
    black_ford = Car("ford", "black", "hatchback") -> {black_ford}
    bmw_motorcycle = Motorcycle("bmw", "blue", False) -> {bmw_motorcycle}
Possiamo controllare tramite la funzione isinstance che sono effettivamente degli oggetti di tipo Vehicle:
    isinstance(black_ford, Vehicle) -> {car_is_vehicle}
    isinstance(bmw_motorcycle, Vehicle) -> {motorcycle_is_vehicle}
    """
    print(text_inheritance)

    text_methods_and_fields = f"""Per ora abbiamo visto la prima implicazione immediata di inheritance: se una class A eredita da una classe B,
allora tutte le istanze di A sono anche istanze di B. C'è però un'altra importante implicazione: le istanze della classe figlia (quella che eredita), ha
accesso a tutti i metodi e campi della classe genitore (quella da cui eredita). Nel nostro caso gli oggetti Car e Motorcycle hanno accesso ai campi
make e color, e al metodo repaint.
    black_ford.make -> {black_ford.make}
    black_ford.color -> {black_ford.color}
    bmw_motorcycle.make -> {bmw_motorcycle.make}
    bmw_motorcycle.color -> {bmw_motorcycle.color}
"""
    print(text_methods_and_fields)

    text_repaint_car = """Eseguiamo il metodo repaint sull'oggetto di tipo Car:
    black_ford.repaint("dark blue")"""
    print(text_repaint_car)
    black_ford.repaint("dark blue")
    text_repaint_motorcycle = """
E ora sull'oggetto di tipo Motorcycle:
    bmw_motorcycle.repaint("grey")"""
    print(text_repaint_motorcycle)
    bmw_motorcycle.repaint("grey")

    text_init = """Per implementare correttamente l'ereditarietà fra classi bisogna prestare attenzione al metodo __init__ della 
classe figlio. Consideriamo il metodo __init__ della classe Car:
    Class car:
        def __init__(self, make, color, body_type):
            super().__init__(make, color)
            self.body_type = body_type
Oltre al parametro self, questo __init__ ha 3 parametri: make, color, e body_type. Dovremo quindi passere ciascuno di questi argomenti nel costruttore
ogni volta che andremo a creare un oggetto di tipo Car. Questi argomenti vengono gestiti in modo differente. Gli argomenti make e color vengono a loro
volta passati al metodo __init__ della classe Vehicle (super() dà accesso ai metodi della classe genitore), mentre body_type viene gestito direttamente 
dall'__init__ della classe Car (poichè è un campo tipico degli oggetti di tipo Car, ma non di un oggetto Vehicle qualunque).
Osserviamo il metodo __init__ della classe Vehicle:
    class Vehicle:
        def __init__(self, make, color):
            print("called __init__ from class Vehicle")
            self.make = make
            self.color = color
ho inserito un istruzione che stampa del testo ogni volta che questo metodo viene chiamato. Quindi, dovremmo vedere quel testo stampato ogni volta che
creaimo un oggetto di tipo Vehicle (quindi anche un Car o un Motorcycle).
    """
    print(text_init)
    print('Creiamo un Car con Car("ford", "black", "hatchback"):')
    Car("ford", "black", "hatchback")
    print('Creiamo un Motorcycle con Motorcycle("bmw", "blue", False):')
    Motorcycle("bmw", "blue", False)
