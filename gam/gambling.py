import gra

def add_user_to_file(filename, nick, imie, nazwisko, haslo, balans):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{nick},{imie},{nazwisko},{haslo},{balans}\n")






def read_user_file(filename):
    users = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                nick, imie, nazwisko, haslo, balans = line.split(',')
                user = {
                    "nick": nick.strip(),
                    "Imie": imie.strip(),
                    "nazwisko": nazwisko.strip(),
                    "Hasło": haslo.strip(),
                    "Balans": float(balans.strip())
                }
                users.append(user)
    
    return users

u = read_user_file("users.txt")


def logowanie():
    user = None
    z = 0
    while z != 1:
        nick = input("Podaj nick: ")
        haslo = input("Podaj haslo: ")
        for i in u:
            if i["nick"] == nick and i["Hasło"] == haslo:
                print(f"Witamy {i['Imie']} {i['nazwisko']} \n\n\n")
                
                user = i
                z = 1
                break
        if z != 1:
            print("Podałeś złe dane")
    granie = gra.main(nick, i["Balans"])
    if granie == -1:
        print("Coś poszło nie tak")

def main():
    print("Witamy w kasynie")
    wybur = input("1.) Loguj \n2.) Rejestruj\n")
    if wybur == "1":
        logowanie()
    if wybur == "2":
        nick = input("Podaj swój nick: ")
        imie = input("Podja swoje imie: ")
        nazwisko = input("Podaj swoje nazwisko: ")
        haslo = input("Podaj swoje hasło: ")
        balans = float(input("ile chesz wpłacić: "))
        add_user_to_file("users.txt", nick, imie, nazwisko, haslo, balans)
        



if __name__ == "__main__":
   main()
