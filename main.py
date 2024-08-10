#!/usr/bin/python3

import sys
import time
import os
from colorama import Fore, init

class mode():
    
    # rutas del sitema
    HOME = "/home/user"
    RUTE = "/home/user/dev"

    # colores para perzonalizar
    init(autoreset=True)

    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUES = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE

    TIMER = time.sleep(1.5)

    def load(total, duracion):
        
        inicio = time.time()
        flecha = '→'
        espacio = ' '
    
        while time.time() - inicio < duracion:
            progreso = (time.time() - inicio) / duracion
            pos_flecha = int(progreso * total)
            
            # Construir la barra con la flecha en la posición correspondiente
            barra = espacio * pos_flecha + flecha + espacio * (total - pos_flecha - 1)
            # Mostrar la barra de progreso en la misma línea
            sys.stdout.write(f'\r[{barra}] {int(progreso * 100)}%')
            sys.stdout.flush()
            time.sleep(0.1)    
        sys.stdout.write('\n')


    def OpenNvim(rute = str):
        os.system('clear')
        os.system(f"nvim {rute}")

    def dev():
        os.chdir(mode.HOME)
        os.system("clear")
        py = ["src", "doc"]
        files = ["main.py", "README.md"]

        checkrute = os.path.exists(mode.RUTE)
        if checkrute is False:
            print(mode.YELLOW + "[!] Developer path was not found")
            mode.TIMER
            print(mode.YELLOW + "[!] Creating the directory")
            os.mkdir("dev")
            mode.TIMER
            print(mode.GREEN + "\n[+] Directory created successfully")
        else:
            mode.TIMER
            print(mode.GREEN + "\n[+] Developer path found successfully")
        while True:
            os.chdir(mode.RUTE)
            pry = input(mode.WHITE + "\nName of the proyect \n > ")
            checkproyectname = os.path.exists(pry)
            if checkproyectname is True:
                print(mode.YELLOW + "[!] The project already exists")
            else:
                os.mkdir(pry)
                os.chdir(f"{mode.RUTE}/{pry}")
                print(mode.CYAN + "[*] Creating the python virtual environment")
                os.system("python -m venv env")
                break 
        for direc in py:
            os.mkdir(direc)
        for d in py:
            os.chdir(f"{mode.RUTE}/{pry}")         
            for f in d:
                os.chdir(f"{mode.RUTE}/{pry}/src")
                os.system(f"touch {files[0]}")
                for i in files:
                    os.chdir(f"{mode.RUTE}/{pry}/doc")
                    os.system(f"touch {files[1]}")

        urldev = f"{mode.RUTE}/{pry}/{py[0]}/{files[0]}"        
        mode.TIMER
        print(mode.GREEN + "[+] Environment ready \n" + mode.MAGENTA+"Opening Nvim")
        mode.barra_progreso_flecha(total=40, duracion=5)
        mode.OpenNvim(rute = urldev)
    def returnP():
        os.system("clear")
        listp = os.listdir(mode.RUTE)
        counter = 1

        print(mode.MAGENTA + "[Proyects]")
        
        for proyects in listp:
            print(mode.WHITE + f"{counter}. {proyects}")
            counter += 1

        select = input("> ")

        if select in listp:
            mode.TIMER
            os.system("clear")
            print(mode.GREEN + f"[+] seleccionaste el proyecto {select}\n")
            mode.TIMER

            os.system(f"tree {mode.RUTE}/{select}/src")
            proyectUrl = f"{mode.RUTE}/{select}/src/main.py"
            
            print(mode.MAGENTA + "\n[+] Cargando el Proyecto")
            print(mode.MAGENTA + "[+] Opening NeoVim ")

            mode.barra_progreso_flecha(total=40, duracion=5)

            mode.OpenNvim(proyectUrl)
        else:
            os.system("clear")
            print(mode.YELLOW + f"[i] The project does not exist, create it")
            mode.dev()
    
    def ProjectValidator():
        try:
            listproyects = os.listdir(f"{mode.RUTE}")
            if len(listproyects) > 0:
                return True
            else: 
                print(mode.YELLOW + "[i] First create a project there is no project stored on the computer")
                mode.dev()
        except FileNotFoundError:
            print(mode.YELLOW + "[i] First create a project there is no project stored on the computer")
            mode.dev()

if __name__ == "__main__":
    os.system("clear")

    NAMEUSER = "SKULL"

    print(mode.WHITE+"Hello "+mode.MAGENTA + NAMEUSER +mode.WHITE+", are we going to program a new script or resume a previous project?\n\n[1] Nuevo poyecto \n[2] Retoma de proyecto anterior")

    while True:
        
        try:
            option = int(input("> "))
            if option in range(1,3):
                if option == 1:
                    mode.dev()
                    break
                if mode.ProjectValidator() is True:
                    mode.returnP()
                    break
            else:
                print(mode.YELLOW + "[!] Error options are 1 or 2")
        except ValueError:
            print(mode.YELLOW + "[!] Do not write values that are not in the options")
        except KeyboardInterrupt:
            break 


