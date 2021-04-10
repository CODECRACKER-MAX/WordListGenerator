# Word List Creator!
import itertools
import os
import platform
import time

if platform.system() == "Windows":
    print("Your Running A Windows Version!")
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

elif platform.system() == "Linux":
    print("Your Running A Linux Version!")
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


def main_menu():
    print("""
                  _                               _  __          __           _   _      _     _      _____                           _             
         /\      | |                             | | \ \        / /          | | | |    (_)   | |    / ____|                         | |            
        /  \   __| |_   ____ _ _ __   ___ ___  __| |  \ \  /\  / /__  _ __ __| | | |     _ ___| |_  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
       / /\ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` |   \ \/  \/ / _ \| '__/ _` | | |    | / __| __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
      / ____ \ (_| |\ V / (_| | | | | (_|  __/ (_| |    \  /\  / (_) | | | (_| | | |____| \__ \ |_  | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
     /_/    \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_|     \/  \/ \___/|_|  \__,_| |______|_|___/\__|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|    by Steven """)

    print("""\t\t\t\t
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  __  __      _        __  __              
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t |  \/  |__ _(_)_ _   |  \/  |___ _ _ _  _ 
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t | |\/| / _` | | ' \  | |\/| / -_) ' \ || |
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t |_|  |_\__,_|_|_||_| |_|  |_\___|_||_\_,_|
                                           
""")
    print("Please Select A Options from the following options ;) ")
    print("1. Numeric Word List Generator Only")
    print("2. String  Word List Generator Only")
    print("3. Numeric & String Word List Generator")
    print("4. Customized Creator Only")
    print("5. About The Developer ")

    try:
        global usr_choice
        usr_choice = int(input("Enter your choice: "))
    
    except ValueError:
        print("Error! Please Select From The Following Option's, 1/2/3")
        main_menu()

    wordlist_creator()
                

def wordlist_creator():
    if (usr_choice == 1):
        chrs = '0123456789'
        pass
    
    elif (usr_choice == 2):
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        pass

    elif (usr_choice == 3):
        chrs = "0123456789abcdefghijklmnopqrstuvwxyz"
        pass

    elif (usr_choice == 4): # Random WordList Creator !

        print("Enter all the character you want to include in your word list:\nExample: abcdefghijklmnopqrstuvwxyz0123456789@%!#$^%$(&*)\n ")
        chrs =input("Enter your choice: ")

    elif (usr_choice == 5):
        print("Hey, My Name Is Steven And I Love To Code and Hack ;) ")
        print("Well, That's much pretty much about my self, going back to main menu!")
        time.sleep(5)
        main_menu()

    else:
        print("Error! We Don't Have {} Option with us!".format(usr_choice))
        main_menu()

    try:
        min_length = int(input("Enter the minimum value you want: ")) # Max characters
        max_length = int(input("Ente the maximum value you want: ")) # Minimum characters

    except ValueError:
        print("Error!, Please enter you the value in numeric type!")
        
    wordlist_ = open("WordList.txt","w+")

    os.system('cls')


    print("Generating Your Word List Please Wait.................")

    for n in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=n):
            wordlist_.write(''.join(xs))
            wordlist_.write("\n")
    print("Done! Creating Wordlist :D")
    print("Your WordList Is Saved On The Desktop, named as - 'WordList.txt' ")
    print("Thanks for using the script, Signing Out Stefen ;)")

main_menu()
