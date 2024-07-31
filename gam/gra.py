from random import randint
from sys import exit
from time import sleep
from os import system

class Gracz:
    def __init__(self, name: str, balans: float) -> None:
        if balans < 0:
            print("Coś poszło nie tak z stanem konta")
            exit(1)
        elif name is None:
            print("Coś poszło nie tak z nikiem")
            exit(1)
        self.name = name
        self.balans = balans
        self.emotki5 = ["🍒", "🍒", "🍒", "🍒", "🍒"]  # 35%
        self.emotki4 = ["🍓", "🍓", "🍓", "🍓"]  # 28%
        self.emotki3 = ["🍇", "🍇", "🍇"]  # 21%
        self.emotki2 = ["🍉", "🍉"]  # 14%
        self.emotki1 = ["🎰"]  # 7%

    def granie(self, stawka: float):
        if stawka <= 0 or stawka > self.balans:
            print("Wpisałeś za mało lub za dużo do stawki")
            return
        else:
            lista = self.emotki1 + self.emotki2 + self.emotki3 + self.emotki4 + self.emotki5
            for i in range(20):
                wl = []
                for j in range(3):  # Zmieniono zmienną sterującą pętlą na 'j'
                    x = randint(0, 14)
                    wl.append(lista[x])
                if i < 15:
                    print(f"{wl[0]}  {wl[1]}  {wl[2]}")
                    sleep(0.2)
                    system("clear")
                elif i >= 15 and i <= 18:
                    print(f"{wl[0]}  {wl[1]}  {wl[2]}")
                    sleep(0.5)
                    system("clear")
                elif i == 19:
                    print(f"{wl[0]}  {wl[1]}  {wl[2]}")
                    print("Poczekaj chwilę...")
                    sleep(0.5)
                    if wl[0] == wl[1] and wl[0] == wl[2]:
                        wygrana = 0
                        match wl[0]:
                            case "🍒":
                                wygrana = stawka * 2
                            case "🍓":
                                wygrana = stawka * 2.3
                            case "🍇":
                                wygrana = stawka * 2.7
                            case "🍉":
                                wygrana = stawka * 3
                            case "🎰":
                                wygrana = stawka * 5
                        if wygrana > 0:
                            print(f"Wygrałeś {wygrana}")
                            self.balans += wygrana
                    else:
                        print(f"Przegrałeś {stawka}")
                        self.balans -= stawka

def main(name: str, balans: float):
    if name == None or balans == None:
        return -1
    print(f"Witamy w grze {name}")
    urzytkownik = Gracz(name, balans)
    print(f"Twój balans to: {urzytkownik.balans}")
    while True:
        odp = input("Wpisz 1 jeśli chcesz zagrać: ")
        print(f"Twój balans to {urzytkownik.balans}")
        if odp == "1":
            stawka = float(input("Ile chcesz postawić: "))
            urzytkownik.granie(stawka)
            sleep(3)
        else:
            break
    

    


