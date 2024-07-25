import os
import shutil

makefile_content = """
# Definicje zmiennych
CC = gcc
CFLAGS = -Wall -Wextra -Iinclude
LDFLAGS = -Llib
LDLIBS = $(wildcard lib/*.a)

SRC_DIR = src
OBJ_DIR = obj
OUT_DIR = out
TARGET = $(OUT_DIR)/program

SRC = $(wildcard $(SRC_DIR)/*.c)
OBJ = $(SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# Cele makefile
all: $(TARGET)

$(TARGET): $(OBJ)
	@mkdir -p $(OUT_DIR)
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c -o $@ $<

# Run the program
run: $(TARGET)
	@echo "Uruchamianie programu..."
	./$(TARGET)

# Clean up
clean:
	rm -rf $(OBJ_DIR) $(OUT_DIR)

.PHONY: all clean run
"""

c_file = """
#include <stdio.h>

//Wpisz w konsoli "make run", żeby skompilować uruchomić projekt
//Wpisz "make clean", żeby usunąć pliki po kompilacji
//Żeby dodać bibliotekę zmodyfikój MEAKFILE


int main(){

    printf("Hello World");
    return 0;
}
"""




def create_project(name: str, user: str):
    base_path = f"/home/{user}/projekty/{name}"
    
    # Sprawdź, czy katalog już istnieje
    if os.path.exists(base_path):
        print(f"Projekt o nazwie {name} już istnieje.")
        return

    os.makedirs(f"{base_path}/src", exist_ok=True)
    os.makedirs(f"{base_path}/lib", exist_ok=True)
    
    makefile_path = os.path.join(base_path, 'Makefile')
    with open(makefile_path, 'w') as file:
        file.write(makefile_content)
    c_f_path = os.path.join(f"{base_path}/src", 'main.c')
    with open(c_f_path, 'w') as file:
        file.write(c_file)

    print(f'Projekt został utworzony w: {base_path}')
    os.system(f"code /home/{user}/projekty/{name}")

def CrPr(user: str, pl: list):
    for idx, proj in enumerate(pl, start=1):
        print(f"{idx}.) {proj}")
    
    while True:
        name = input("Jak chcesz nazwać projekt?\n")
        if name in pl:
            print("Projekt o tej nazwie już istnieje. Wybierz inną nazwę.")
        else:        
            create_project(name, user)
            break

def main(user: str):
    odp = int(input("Chcesz stworzyć czy usunąć projekt (1 = stworzyć / 2 = usunąć / inny przycisk kończy program): "))
    
    if odp == 1:
        pl = os.listdir(f"/home/{user}/projekty")
        CrPr(user, pl)
    elif odp == 2:
        pl = os.listdir(f"/home/{user}/projekty")
        for idx, proj in enumerate(pl, start=1):
            print(f"{idx}.) {proj}")
        
        z = int(input("Podaj numer projektu, który chcesz usunąć: "))
        if 1 <= z <= len(pl):
            n = pl[z - 1]
            try:
                shutil.rmtree(f"/home/{user}/projekty/{n}")
                print(f"Projekt {n} został usunięty.")
            except Exception as e:
                print(f"Wystąpił błąd podczas usuwania projektu: {e}")
        else:
            print("Niepoprawny numer projektu.")
    else:
        print("Do widzenia :)")


if __name__ == "__main__":
    user = os.getlogin()
    projekty_path = f"/home/{user}/projekty"
    
    if not os.path.exists(projekty_path):
        os.makedirs(projekty_path)

    pl = os.listdir(projekty_path)
    
    print(f"Witaj {user}")
    for idx, proj in enumerate(pl, start=1):
        print(f"{idx}.) {proj}")
    
    main(user)
