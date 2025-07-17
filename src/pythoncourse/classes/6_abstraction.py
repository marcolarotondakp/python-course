from abc import ABC, abstractmethod
from typing_extensions import override


class Vehicle(ABC):
    def __init__(self, make, color):
        self.make = make
        self.color = color

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def __init__(self, make, color):
        super().__init__(make, color)

    @override
    def drive(self):
        print("I am driving the car")


class Motorcycle(Vehicle):
    def __init__(self, make, color):
        super().__init__(make, color)

    @override
    def drive(self):
        print("I am driving the motorcycle")


if __name__ == "__main__":
    type_error = None
    try:
        Vehicle("ford", "black")
    except TypeError as e:
        type_error = str(e)
    assert isinstance(type_error, str)
    text_abstraction = f"""Supponiamo di voler modellare il fatto che non esistono veicoli generici, ma 
solo veicoli di un tipo specifico. Non esistono veicoli e basta, ma esistono veicoli che sono automobili,
moto, elicotteri, aerei, ecc. Per modellare questo fatto bisogna sfruttare il concetto di abstraction, che
consiste in implementare una classe astratta (ovvero che non può essere direttamente istanziata), e implementare
successivamente classi concrete che ereditano dalla classe astratta. Affinchè sia considerata astratta, una classe python
deve:
    - ereditare dalla classe abc.ABC (sta per Abstract Base Class)
    - implementare almeno un metodo astratto tramite il decoratore @abc.abstractmethod
La classe Vehicle è quindi una classe astratta:
    class Vehicle(ABC):
        ...
        @abstractmethod
        def drive(self):
            pass
Verifichiamo che la classe Vehicle non può essere istanziata direttamente. Se proviamo a eseguire
    Vehicle("ford", "black")
otteniamo un TypeError con messaggio di errore
    {type_error}
che ci dice che non possiamo istanziare la classe Vehicle, perchè non abbiamo fornito un'implementazione
concreta del metodo drive.
    """
    print(text_abstraction)

    car = Car("ford", "black")
    motorcycle = Motorcycle("bmw", "blue")
    text_concrete = f"""Le classi Car e Motorcycle ereditano da Vehicle e forniscono un'implementazione concreta del metodo drive.
Possiamo quindi istanziarle
    car = Car("ford", "black") -> {car}
    motorcycle = Motorcycle("bmw", "blue") -> {motorcycle}
"""
    print(text_concrete)
