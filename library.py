# This library management uses a list of dictionaries to store the books.

# You are able to check out, check in, and check out books.

# You are also able to print all the books in the system regardless of their status (in or out).

# Finally, you are able to search up and book and see its status in the system.

import pprint
import os
import time

# All Books, Both Checked out and Not 
allBooks =[

{'ID': 101, 'title': 'Meditations',           'author': 'Marcus Aurelius',          'year': 180,},
{'ID': 102, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee',               'year': 1960,},
{'ID': 103, 'title': 'The Great Gatsby',      'author': 'F. Scott Fitzgerald',      'year': 1925,},
{'ID': 104, 'title': 'Don Quixote',           'author': 'Miguel de Cervantes',      'year': 1615,},
{'ID': 105, 'title': 'The Little Prince',     'author': 'Antoine de Saint-Exupery', 'year': 180,}

]

# Books in the system
booksCurrentlyInSystem = [
    
{'ID': 102, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee',               'year': 1960,},
{'ID': 103, 'title': 'The Great Gatsby',      'author': 'F. Scott Fitzgerald',      'year': 1925,},
{'ID': 104, 'title': 'Don Quixote',           'author': 'Miguel de Cervantes',      'year': 1615,},
{'ID': 105, 'title': 'The Little Prince',     'author': 'Antoine de Saint-Exupery', 'year': 180,}

]

# Books Checked Out
booksCheckedOut =[

{'ID': 101, 'title': 'Meditations',  'author': 'Marcus Aurelius',  'year': 180}

]

menu = ' ------ Main Menu ------ \n\n 1. All Books \n 2. Check In \n 3. Check Out \n 4. Look Up \n\n'


#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################



# Printing All Books 
def menu1():

    # Clears Terminal, Prints Dictionary Line by Line, Prompts User to go Back
    os.system('clear')   
    for dic in allBooks:
        print(dic)
    option = input('\nType 0 to go back: ')

    # Going Back to Main Menu 
    if option == '0':
        os.system('clear')
        return main_menu()

    # If User Doesn't Go Back We Will Reset to menu1()
    else:
        return menu1()



# Checking In Books 
def menu2():

    #  Starting Menu, Print All Books Checked Out Line By Line
    #  Prompt User For Either 0 (return), Or An ID
    os.system('clear')
    print("Books Currently Checked Out\n-----------------------------\n")
    for books in booksCheckedOut:
        print(books)
    option = input('\n-----------------------------\nTo Go Back Enter: 0\n\nWhich ID? ')

    # Going back to Main Menu
    if option == '0':
        return main_menu()

    # If User Proceeds with Checking in
    else:

        id = int(option)

        # Iterate through books for the ID the User Gave
        # If we can find it, we will append that dictionary to booksCurrentlyInSystem
        # If we don't find it, it will show a message and take user back to main_menu()
        for books in booksCheckedOut:
            if books['ID'] == id:
                booksCurrentlyInSystem.append(books)
                booksCheckedOut.remove(books)
                os.system('clear')
                print(f'\nID: {id} has been checked in.')
                print('\n\nThank you, please wait.\n')
                time.sleep(3)
                return main_menu()

            # If ID Isn't Found in Books Currently in System, we will show message and take back to menu2()
            else:
                
                os.system('clear')
                print(f'\nID: {id} not found')
                time.sleep(3)
                return main_menu()



# Checking out books 
def menu3():

    # Starting Menu, Print all Books in System, and Prompt User for either 0 (return), or an ID
    os.system('clear')
    print("Books Currently Ready to Check Out\n-----------------------------\n")
    for books in booksCurrentlyInSystem:
        print(books)
    option = input('\n-----------------------------\nTo Go Back Enter: 0\n\nWhich ID? ')

    # Going Back to Main Menu 
    if option == '0':
        os.system('clear')
        print('\nReturning, Please Wait')
        time.sleep(3)
        return main_menu()

    else:
        id = int(option)

        # Iterate through Books to find an ID Equal to User given ID
        # If we find it we will append the book into booksCheckedOut and remove from booksCurrentlyinSystem
        # If we don't find it, it will show a message and prompt user again
        for books in booksCurrentlyInSystem:
            if books['ID'] == id:
                booksCheckedOut.append(books)
                booksCurrentlyInSystem.remove(books)
                os.system('clear')
                print(f'\nID: {id} has been checked out.')
                print('\n\nThank you, please wait.\n')
                time.sleep(3)
                return main_menu()
            
            # If ID isn't found we will show message and take user back to menu3()
            else:
                os.system('clear')
                print(f'\nID: {id} not found')
                time.sleep(3)
                return menu3()



# Looking up books in system and their Status
def menu4():

    # Starting Menu, Will Print Welcome, Prompt User for ID
    os.system('clear')
    print('Welcome to the Look-Up Tool\n\nTo Return Enter 0\n\nPlease enter the ID of the Book you would like to search up\n\n')
    option = input('ID: ')
    
    # If user wants to return
    if option == '0':
        os.system('clear')
        print('\nReturning, Please Wait')
        time.sleep(3)
        return main_menu()
    
    else:
        
        id = int(option)

        # Iterate through booksCurrentlyInSystem To Find If Book Is Read To Check Out
        for books in booksCurrentlyInSystem:
            if books['ID'] == id:
                os.system('clear')
                print(f'Book: {id} is currently ready to check out!')
                print('\n\nPlease Answer Y or N')
                goBack = input('\n\nWould you like to check it out?')

                # # If Found, Prompt User If They Want To Check Out
                # If They Do, We Will Check Out And Go Back To main_menu()
                if goBack == 'Y':
                    booksCheckedOut.append(books)
                    booksCurrentlyInSystem.remove(books)
                    os.system('clear')
                    print(f'\nID: {id} has been checked out.')
                    print('\n\nThank you, please wait.\n')
                    time.sleep(3)
                    return main_menu()
        
        # If Book Is Checked Out, It Will Take You Back To menu4()
        for books in booksCheckedOut:
            if books['ID'] == id:
                os.system('clear')
                print(f'Sorry, Book: {id} is currently checked out.')
                print('\n\nReturning, Please Wait')
                return menu4()



# This Is The Main Menu 
def main_menu():
    
    # Clear Screen, Print the Main Menu, and Prompt user for Option.
    os.system('clear')   
    print(menu)
    option = input('\nChoose option: ')

    # Will Send User to menu1
    if option == '1':
        os.system('clear')
        return menu1()
    
    # Will send User to menu2
    if option == '2':
        os.system('clear')
        return menu2()

    # Will send User to menu3
    if option == '3':
        os.system('clear')
        return menu3()
    
    # Will send User to menu4
    if option == '4':
        os.system('clear')
        return menu4()

    # If User Chooses anything but one of the options it will reset back to mainMenu
    return main_menu()
      
      
os.system('clear')      
main_menu()

