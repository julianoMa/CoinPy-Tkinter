# Chargement des modules
from tkinter import *
import requests
from tkinter.messagebox import *
print("Chargement des modules..")


class Bitcoine(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Bitcoin Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix du Bitcoin est de " +
                      str(self.getBTCPrice()) + "€")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["BTCEUR"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix du Bitcoin")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()


class Bitcoins(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Bitcoin Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix du Bitcoin est de " +
                      str(self.getBTCPrice()) + "$")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["BTCUSDT"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix du Bitcoin")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()


class Ethereume(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Ethereum Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix de l'Ethereum est de " +
                      str(self.getBTCPrice()) + "€")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["ETHEUR"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix de l'Ethereum")
        return round(float(data['price']))

    def close(self):
        self.destroy()
        Index()


class Ethereums(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Ethereum Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix de l'Ethereum est de " +
                      str(self.getBTCPrice()) + "$")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["ETHUSDT"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix de l'Ethereum")
        return round(float(data['price']))

    def close(self):
        self.destroy()

class Litecoine(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Litecoine Price")
        self.geometry("500x200")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Accueil", command=self.close)
        menu.add_command(label="Quitter", command=quit)

        label = Label(self, text="Le prix du Litecoin est de " +
                      str(self.getBTCPrice()) + "€")
        label.pack()

        self.config(menu=menu)
        self.mainloop()

    def getBTCPrice(self):
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        currencies = ["LTCEUR"]
        j = 0
        for i in currencies:
            url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1

        print("Récupération du prix du Litecoin")
        return round(float(data['price']))

    def close(self):
        self.destroy()

class Index(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title("Accueil")
        self.geometry("1000x600")

        self.window()

    def window(self):
        menu = Menu(self)

        menu.add_command(label="Quitter", command=quit)
        menu.add_command(label="Bitcoin (€)", command=self.bitcoine)
        menu.add_command(label="Bitcoin ($)", command=self.bitcoins)
        menu.add_command(label="Ethereum (€)", command=self.ethereume)
        menu.add_command(label="Ethereum ($)", command=self.ethereums)
        menu.add_command(label="Aptos (€)", command=self.aptose)
        
        self.config(menu=menu)
        self.mainloop()

    def bitcoine(self):
        self.destroy()
        Bitcoine()

    def bitcoins(self):
        self.destroy()
        Bitcoins()

    def ethereume(self):
        self.destroy()
        Ethereume()

    def ethereums(self):
        self.destroy()
        Ethereums()

    def aptose(self):
        self.destroy()
        Aptose

print("Chargement de la page d'Accueil..")
window = Index()