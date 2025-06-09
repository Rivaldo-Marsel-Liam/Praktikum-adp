import os
import time
from termcolor import colored

def tampilkan_data_diri():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("="*50, 'blue'))
    print(colored("                      DATA DIRI ", 'yellow', attrs=['bold']))
    print(colored("="*50, 'blue'))
    print(colored("Nama     : Rivaldo Marsel Liam", 'cyan'))
    print(colored("NIM      : 2410431026", 'cyan'))
    print(colored("Shift    : 1", 'cyan'))
    print(colored("Modul    : 9", 'cyan'))
    print(colored("="*50, 'blue'))
    time.sleep(5)#3
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_screen():
    print(colored(r"""
 __  __    _    ____   _____  ______  ___
|  \/  |  / \  |  _ \ /  ___| | ____| | |
| |\/| | / _ \ | |_) |\___  \ |  _|   | |  
| |  | |/ ___ \|  _ < | __) | | |___  | |___ 
|_|  |_/_/   \_\_| \_\|_____/ |_____| |_____|
                  
""", 'yellow', attrs=['bold']))
   
   
    
    print(colored("="*50, 'blue'))
    print(colored("                   MARSEL APLIKASI", 'yellow', attrs=['bold']))
    print(colored("                    Versi 1.0.0", 'green'))
    print(colored("="*50, 'blue'))
    
   
    spinner = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    for i in range(101):
        time.sleep(0.05)
        progress = i//2
        bar = colored('█' * progress + '░' * (50 - progress), 'green')
        print(f"\r{spinner[i%8]} {i:3}% {bar}", end='', flush=True)
    
    print("\n\n" + colored("Aplikasi berhasil dibuka!", 'green', attrs=['bold']))
    time.sleep(5)#1,5
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_utama():
 
    print(colored("APLIKASI SIAP DIGUNAKAN", 'red', attrs=['bold']))
    print(colored("="*25, 'blue'))
   
    # Tambahkan logika aplikasi di sini

if __name__ == "__main__":
    tampilkan_data_diri()
    loading_screen()
    menu_utama()