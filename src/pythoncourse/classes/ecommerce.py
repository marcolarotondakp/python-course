"""
Crea un sistema e-commerce costituito dai componenti: Prodotto, Carrello, Magazzino.

Obiettivo: il sistema deve dimostrare tutti e quattro i principi della programmazione orientata agli oggetti
(inheritance, abstraction, encapsulation, polymorphism).

Requisiti tecnici.
    Ogni prodotto deve avere un nome, un prezzo, e un codice identificativo.
    Assicurati che il prezzo sia un numero positivo.
    Infine, ogni prodotto deve avere una funzionalità che consentee di calcolare
    il costo di spedizione per quel prodotto.
    Ogni tipo specifico di prodotto deve avere almeno una caratteristica specifica.

    Il magazzino deve tenere traccia, per ogni prodotto, di quante copie ne sono disponibili.
    (usa un campo di tipo dizionario)
    Deve avere due funzionalità: aggiungere e rimuovere prodotti dal magazzino.
    Queste funzionalità devono includere anche un'istruzione print adeguata

    Il carrello deve tenere traccia dei prodotti da acquistare (anche qui, usa un dizionario).
    Deve avere inoltre le seguenti funzionalità:
        - aggiungere e rimuovere i prodotti nel carrello
        - svuotare il carrello
        - acquistare il contenuto del carrello
        - ritornare il costo totale dei prodotti
        - ritornare il costo totale delle spese di spedizione
    Le operazioni sul carrello devono avere un effetto sul magazzino:
        - aggiungere prodotti al carrello deve ridurre la disponibilità nel magazzino
        - rimuovere prodotti dal carrello deve aumentare la disponibilità nel magazzino
    Viceversa, non deve essere possibile aggiungere prodotti nel carrello oltre la disponibiltà nel magazzino.
    Includi, dove e se rilevante, delle istruzioni print adeguante all'interno delle
    funzionalità del carrello.



Ora puoi scrivere un blocco main per provare il programma:
    - crea dei prodotti
    - crea un magazzino
    - aggiungi prodotti al magazzino
    - crea un carrello
    - prova le varie operazioni sul carrello


Prerequisiti extra.
    Operazioni basi sui dizionari (https://www.w3schools.com/python/python_dictionaries.asp).
    Vedi le sezioni:
        - Python Dictionaries
        - Access Items
        - Change Items
        - Add Items
        - Remove Items
    Oppure:
        https://www.coursera.org/learn/python-functions-files-dictionaries/home/module/2 (sezione Dictionary Mechanics)
    O anche:
        Python essentials 1 (pdf su slack) - cap 4.6
"""

from abc import ABC, abstractmethod
from typing_extensions import override


class Prodotto(ABC):
    next_id: int = 0

    def __init__(self, nome: str, prezzo: int) -> None:
        self.nome = nome
        self.prezzo = prezzo
        self.id = Prodotto.next_id
        Prodotto.next_id += 1

    @abstractmethod
    def calcola_spedizione(self) -> int:
        pass

    @override
    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Prezzo: {self.prezzo}"


class Libro(Prodotto):
    def __init__(self, nome: str, prezzo: int, autore: str) -> None:
        super().__init__(nome, prezzo)
        self.autore = autore

    @override
    def calcola_spedizione(self) -> int:
        return self.prezzo // 5


class CD(Prodotto):
    def __init__(self, nome: str, prezzo: int, numero_tracce: int) -> None:
        super().__init__(nome, prezzo)
        self.numero_tracce = numero_tracce

    @override
    def calcola_spedizione(self) -> int:
        return 2


class Magazzino:
    def __init__(self, inventario: dict[Prodotto, int] | None = None) -> None:
        if inventario is None:
            self.inventario = {}
        else:
            self.inventario = inventario

    def add(self, prodotto: Prodotto):
        if prodotto not in self.inventario:
            self.inventario[prodotto] = 1
        else:
            self.inventario[prodotto] += 1
        print(f"Copie di {prodotto}: {self.inventario[prodotto]}")

    def remove(self, prodotto: Prodotto):
        quantity = self.inventario.get(prodotto)
        if quantity is None or quantity == 0:
            print(
                f"non è possibile rimuovere l'oggetto {prodotto}. Copie nell'inventario: {quantity}"
            )
        else:
            self.inventario[prodotto] -= 1


class Carrello:
    def __init__(self, magazzino: Magazzino) -> None:
        self.da_acquistare: dict[Prodotto, int] = {}
        self.costi_prodotti = 0
        self.costi_spedizione = 0
        self.magazzino = magazzino

    def svuota(self) -> None:
        self.da_acquistare.clear()
        self.costi_prodotti = 0
        self.costi_spedizione = 0

    def add(self, prodotto: Prodotto) -> None:
        quantita_magazzino = self.magazzino.inventario.get(prodotto)
        if quantita_magazzino is None or quantita_magazzino == 0:
            print("Impossibile aggiungere prodotto al carrello")
            return
        if prodotto not in self.da_acquistare:
            self.da_acquistare[prodotto] = 1
        else:
            self.da_acquistare[prodotto] += 1
        self.costi_prodotti += prodotto.prezzo
        self.costi_spedizione += prodotto.calcola_spedizione()
        self.magazzino.remove(prodotto)

    def remove(self, prodotto: Prodotto) -> None:
        if prodotto in self.da_acquistare:
            self.da_acquistare[prodotto] -= 1
            self.costi_prodotti -= prodotto.prezzo
            self.costi_spedizione -= prodotto.calcola_spedizione()
            self.magazzino.add(prodotto)
            if self.da_acquistare[prodotto] == 0:
                del self.da_acquistare[prodotto]
