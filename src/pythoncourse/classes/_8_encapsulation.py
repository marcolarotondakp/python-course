from datetime import datetime


class BankAccount:
    next_id = 0

    def __init__(self, name: str, pin: int) -> None:
        self.name = name
        self._creation_date = datetime.now()
        self.__balance = 0
        self.__pin = pin
        self.__authenticated = False
        self._id = BankAccount.next_id
        BankAccount.next_id += 1

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("Authentication completed")
        else:
            print("Wrong pin")

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        if self.__authenticated:
            return self.__balance
        raise Exception("You need to be authorized to check balance")

    @balance.setter
    def balance(self, value):
        if self.__authenticated:
            self.__balance = value
        else:
            raise Exception("You need to be authorized to modify balance")

    def deposit(self, value):
        self.balance += value

    def withdrawal(self, value):
        self.balance -= value


if __name__ == "__main__":
    account: BankAccount = BankAccount(name="Bob", pin=1234)
    text_create_account = """Creiamo l'account di Bob:
    account: BankAccount = BankAccount(name="bob", pin=1234)
    """
    print(text_create_account)
    text_access_modifiers = f"""Questo account (vedi metodo __init__) ha:
    - un campo pubblico (name) <- variabile senza underscore iniziale
    - 2 campo protetto (_id, _creation_date) <- variabile con un solo underscore iniziale
    - 3 campi privati (__balance, __pin, __authenticated) <- variabili con 2 underscore iniziali
Questo è il significato degli access modifiers:
    - pubblico: è accessibile ovunque
    - protected: è accessibile solo all'interno della classe in cui è definito, o all'interno
                 di una classe che eredita da essa
    - private: è accessibile solo all'interno della classe in cui è definito.
    
IMPORTANTE:
    python non ha meccanismi che bloccano veramente l'accesso a campi/metodi, ma gli
    access modifiers sono da intendersi solo come convenzioni per documentare come
    bisogna accedere a un campo. Se definite un campo (e.g.) come privato, state comunicando
    che a quel campo ci si può accedere solo all'interno della classe in cui è definito.
Per esempio, qui sono nel blocco main (quindi non all'interno della classe BankAccount, nè in una
sua subclass). Anche se non dovrei farlo, posso comunque accedere al campo _creation_date:
    account._creation_date -> {account._creation_date}
    """
    print(text_access_modifiers)

    error_private_access = None
    try:
        account.__pin
    except AttributeError as e:
        error_private_access = str(e)
    assert error_private_access is not None
    text_private_modifier = f"""Posso accedere anche ai campi privati?
Se eseguo:
    account.__pin 
Ottengo il seguente errore di typo AttributeError:
    {error_private_access}
Questo succede perchè python, seppur non impedendo formalmente l'accesso al campo privato,
adopera una tecnica chiamata 'name mangling' per evitare accessi non intenzionali al campo.
Questa tecnica consiste nel rinominare il campo prefissandolo con _NomeClasse.
Quindi:
    account._BankAccount__pin -> {account._BankAccount__pin}
Ovviamente, tutto ciò deve scoraggiarci dal chiamare campi e metodi privati al di fuori della
classe in cui sono definiti.
    """
    print(text_private_modifier)

    error_unmodifiable_property = None
    try:
        account.id = 2
    except AttributeError as e:
        error_unmodifiable_property = str(e)
    assert error_unmodifiable_property is not None
    text_property = f"""Il decoratore @property ci viene in aiuto per implementare una 
maggiore protezione dei campi. Per esempio, osserviamo il seguente metodo che abbiamo annotato
con il decoratore @property.
    @property
    def id(self):
        return self._id
Grazie a @property, viene creato un nuovo campo, id, e nel corpo del metodo annotato è definita la logica
con cui accedere a questo campo, in questo caso ritorna semplicimente il campo _id (ma si può implementare
una logica anche più sofisticata, in base alle necessità). 
Proviamo a ispezionare il nuovo campo:
    account.id -> {account.id}
Di default, il campo definito con @property non è modificabile.
Se provo a sovrascrivere il campo id
    account.id = 2
ottengo un errore di tipo AttributeError con il seguente messaggio:
    {error_unmodifiable_property}"""
    print(text_property)

    error_unauthenticated_user_get = None
    try:
        account.balance
    except Exception as e:
        error_unauthenticated_user_get = str(e)
    assert error_unauthenticated_user_get is not None
    error_unauthenticated_user_set = None
    try:
        account.balance = 500
    except Exception as e:
        error_unauthenticated_user_set = str(e)
    assert error_unauthenticated_user_set is not None
    text_property_continued = f"""
Se vogliamo avere una @property che sia modificabile dobbiamo implementare un setter, per esempio come abbiamo 
fatto per il campo balance:

    @property
    def balance(self):
        if self.__authenticated:
            return self.__balance
        raise Exception("You need to be authorized to check balance")

    @balance.setter
    def balance(self, value):
        if self.__authenticated:
            self.__balance = value
        else:
            raise Exception("You need to be authorized to modify balance")

Se proviamo ad accedere al campo balance otteniamo un errore, perchè non siamo autenticati:
    account.balance -> {error_unauthenticated_user_get}
Abbiamo un errore analogo se proviamo a modificare il campo balance:
    account.balance = 500 -> {error_unauthenticated_user_set}
Fai attenzione ai diversi messaggi di errore: quando si accede al camo balance, viene utilizzata la logica
definita in @property, quando si assegna un valora al campo, viene utilizzata la logica definita in
@balance.setter.

Procediamo quindi con l'autenticazione:
    account.authenticate(1234) ->"""
    print(text_property_continued)

    account.authenticate(1234)
    account.balance = 2000

    text_set_balance = f"""
Ora possiamo modificare il bilancio:
    account.balance = 2000 
    account.balance -> {account.balance}
    """
    print(text_set_balance)
