#!/usr/bin/env python3
import os
import pip
import sys
import ctypes
import platform
import colorama
import subprocess
from shutil import rmtree

# Platform indepent way to check if user is admin
def is_user_admin():
    """
    Check if the script is being run as root/admin

    Return False if privileges cannot be determined
    """
    if platform.system()=='Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() == 1
        except:
            return False
    
    else:
        try:
            return os.getuid()==0
        except:
            return False


# Uninstall Pip packages in a platform independent way
def uninstall_pip_packages():
    print(colorama.Back.CYAN+colorama.Style.BRIGHT+"[+] Uninstalling Pip packages!"+colorama.Style.RESET_ALL)
    try:
        subprocess.check_call([sys.executable,"-m", "pip", "uninstall","-yr","requirements.txt"])
    except:
        print(colorama.Fore.RED+colorama.Style.BRIGHT+"[!] Failed to uninstall pip packages")
        print(colorama.Style.RESET_ALL)


# Uninstall PIP
def uninstall_pip():
    print(colorama.Back.RED+colorama.Style.BRIGHT+"[+] Uninstalling Pip packages!"+colorama.Style.RESET_ALL)
    try:
        subprocess.check_call([sys.executable,"-m", "pip", "uninstall","-y","pip"])
    except:
        print(colorama.Fore.RED+colorama.Style.BRIGHT+"[!] Failed to uninstall pip")
        print(colorama.Style.RESET_ALL)


# Remove pygoat
def remove_pygoat():
    cwd = os.getcwd()
    print(colorama.Back.RED+colorama.Style.BRIGHT+f"All files in {cwd} will be deleted!"+colorama.Style.RESET_ALL)
    for item in os.listdir(cwd):
        filename = cwd+item
        if(os.path.isfile(filename)):
            try:
                print("[!] Deleted: "+colorama.Fore.RED+colorama.Style.BRIGHT+filename+colorama.Style.RESET_ALL)
                os.remove(filename)
            except IsADirectoryError:
                rmtree(filename)
            except:
                print(colorama.Fore.RED+colorama.Style.BRIGHT+f"[!] Failed To remove: {filename}"+colorama.Style.RESET_ALL)
                pass

def main():
    colorama.init()

    # Check if program is being run as admin
    if(not is_user_admin()):
        print(colorama.Fore.RED+colorama.Style.BRIGHT+"[!] This script must be run as root!")
        print(colorama.Style.RESET_ALL)
        sys.exit(-1)

    # Remove pip packages
    uninstall_pip_packages()

    # Remove pip
    choice = input("Uninstall pip? (y/N)")
    if (choice.upper()=='Y' or choice.upper()=='YES'){
        uninstall_pip()
    }
    else{
        print(colorama.Back.CYAN+colorama.Style.BRIGHT+"[+] Pip has been kept intact"+colorama.Style.RESET_ALL)
    }

    # Remove pygoat files
    choice = input("Would you like to remove all pygoat directories and files? (y/N)")
    if (choice.upper()=='Y'or choice.upper()=='YES'){
        remove_pygoat()
        choice2 = input(f"Remove {os.getcwd}? (y/N)")
        if (choice2.upper()=='Y'or choice2.upper()=='YES'){
            rmtree(os.getcwd())
            print(colorama.Back.RED+colorama.Style.BRIGHT+f"[+] {os.getcwd()} has been removed"+colorama.Style.RESET_ALL)
    }
    else{
        print(colorama.Back.CYAN+colorama.Style.BRIGHT+f"[+] {os.getcwd()} has been kept intact"+colorama.Style.RESET_ALL)
    }

    # Restore output streams to their original values
    colorama.deinit()

if __name__ == '__main__':
    main()