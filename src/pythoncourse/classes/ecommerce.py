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
