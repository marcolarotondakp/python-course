class Vehicle:
    def __init__(self, make, color):
        self.make = make
        self.color = color

    def repaint(self, new_color):
        print("Repainting the car...")
        self.color = new_color
        print(f"Now the car is {new_color}!")


if __name__ == "__main__":
    is_a_type = isinstance(Vehicle, type)
    text_class = f"""Vehicle è una classe, infatti è del tipo 'type':
    isinstance(Vehicle, type) -> {is_a_type}
    """
    print(text_class)

    black_ford = Vehicle("ford", "black")
    text_create_instance = """Possiamo creare un'istanze della classe nel seguente modo:
    black_ford = Vehicle("ford", "black")\n
Ora la variabile black_ford punta a un oggetto di tipo Vehicle, e questo possiamo vederlo eseguendo
    print(black_ford):"""
    print(text_create_instance)
    print(black_ford)

    is_a_vehicle = isinstance(black_ford, Vehicle)
    text_is_vehicle = f"""
Inoltre possiamo verificare sempre con la funzione isinstance che black_ford è di tipo Vehicle:
    isinstance(black_ford, Vehicle) -> {is_a_vehicle}
    """
    print(text_is_vehicle)

    text_fields = f"""Ogni volte che creiamo un nuovo oggetto usando il costruttore della classe,
i.e. con la notazione Vehicle("ford", "black"), viene chiamato il metodo __init__, che si occupa
di inizializzare i campi della classe in base agli argomenti passati nel costruttore.
Nota: il parametro 'self' si riferisce all'istanza corrente, non si riferisce ad alcun argomento 
passato nel costruttore.
Possiamo ispezionare i campi del veicolo appena creato:
    black_ford.make -> {black_ford.make}
    black_ford.color -> {black_ford.color}
"""
    print(text_fields)

    text_methods = """Quando creaiamo un oggetto, questo ha accesso ai metodi definiti nella classe, in questo caso
al metodo repaint. Questo è un instance method, perchè accede a un'istanza della classe (e in questo caso modifica anche).
Nota: come nel caso del metodo __init__, il primo parametro degli instance method è sempre self.
Possiamo chiamare l'instance method che abbiamo definito nel seguente modo:
    black_ford.repaint("blue")
    """
    print(text_methods)
    black_ford.repaint("blue")

    text_dot_notation = """
Quando chiamiamo un instance method usando la dot notation come abbiamo appena fatto, i.e. in:
    black_ford.repaint("blue")
python è in grado di inferire  l'argomento che sostituisce il parametro self durante la chiamata al methodo: in questo caso self è l'oggetto black_ford
    """
    print(text_dot_notation)
