class Vehicle:
    next_serial = 0

    def __init__(self, make, color):
        self.make = make
        self.color = color
        self.serial = Vehicle.next_serial
        Vehicle.next_serial += 1


if __name__ == "__main__":
    text_variables = """Come ci sono instance methods e class methods, ci sono anche instance variables e class variables.
    """
    print(text_variables)

    black_ford = Vehicle("ford", "black")
    text_instance_variables = f"""Le variabili di istanza sono possedute dalle istanze della classe, e non dalla classe stessa.
Per ogni oggetto di tipo Vehicle, possiamo accedere alle sue proprietà tramite le variabili make, color, e serial.
    black_ford.make -> {black_ford.make}
    black_ford.color -> {black_ford.color}
    black_ford.serial -> {black_ford.serial}
    """
    print(text_instance_variables)

    attribute_error = None
    try:
        Vehicle.make
    except AttributeError as e:
        attribute_error = str(e)
    assert isinstance(attribute_error, str)
    text_attribute_error = f"""Se proviamo ad accedere a una variabile di istanza a partire dalla classe otteniamo un AttributeError:
    Vehicle.make -> {attribute_error}
Questo errore ci dice esattamente che la classe Vehicle (che è un oggetto di tipo 'type') non ha alcun attributo di nome 'make'
    """
    print(text_attribute_error)

    text_class_variables = f"""Le variabili di classe sono proprietà della classe. Nel nostro caso abbiamo la variabile next_serial:
    Vehicle.next_serial -> {Vehicle.next_serial}
Come nel caso dei class methods, possiamo accedere alle variabili di classe attraverso un'istanza della classe:
    black_ford.next_serial -> {black_ford.next_serial}
Per motivi di chiarezza, è generalmente meglio accedere alle variabili di classe tramite la classe stessa.
    """
    print(text_class_variables)

    text_class_variables_use_case = """Un comune uso delle variabili di classe è quando vogliamo che ci sia controllo centralizzato di un dato.
Nel nostro caso next_serial è una variabile gestita dalla classe, in modo tale che sia garantito che due veicoli diversi abbiano necessariamente un seriale diverso.
Se invece il seriale fosse un parametro da passare nel costruttore, allora sarebbe in principio possibile creare macchine diverse con lo stesso seriale.
Assumendo un metodo __init__ definito come:
    def __init__(self, make, color, serial):
        self.make = make
        self.color = color
        self.serial = serial
potremmo ottenere due macchine con lo stesso seriale nel seguente modo:
    Vehicle("ford", "black", 1)
    Vehicle("bmw", "blue", 1)
    """
    print(text_class_variables_use_case)
