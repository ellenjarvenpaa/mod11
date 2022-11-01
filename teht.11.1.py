# yliluokka

class Julkaisu:
    def __init__(self, name):
        self.name = name

# aliluokka

class Kirja(Julkaisu):
    def __init__(self, name, author, page_amount):
        super().__init__(name)
        self.author = author
        self.page_amount = page_amount

    def tulosta_tiedot(self):
        print(f"Book name: {self.name}, author: {self.author}, number of pages: {self.page_amount}")

# aliluokka

class Lehti(Julkaisu):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def tulosta_tiedot(self):
        print(f"Magazine name: {self.name}, editor-in-chief: {self.editor_in_chief}")

# pääohjelma

k = Kirja("Hytti no: 6", "Rosa Liksom", 200)
l = Lehti("Aku Ankka", "Aki Hyyppä")
k.tulosta_tiedot()
l.tulosta_tiedot()
