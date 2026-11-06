import colorama

from colorama import Fore, init

def menu():
    init(autoreset=True)

    print(Fore.CYAN + '''╔══════════════════════════════════════════════╗
║                                              ║
║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
║                                              ║
╚══════════════════════════════════════════════╝''' )
    print(Fore.YELLOW + ''' 1. Add Book 
 2. Viwe Book 
 3. Search Book 
 4. Resister user  
 5. Issued Book 
 6. Exist ''' )


def read_book():
    try:        
        with open("books_info.txt", "r") as f:
                book_data = f.readlines()
                return book_data
    except FileNotFoundError:
        book_data = []
        return book_data

def read_user():
    try:
        with open("user_info.txt", "r") as u:
            user_data = u.readlines()
            return user_data
    except FileNotFoundError:
        user_data = []
        return user_data

    
def read_issued():
        try:

            with open("issued_info.txt", "r") as t:
                user_data = t.readlines()
                return user_data
        except FileNotFoundError:
            user_data = []
            return user_data

def add_book():
    book_data = read_book()
   
    print(Fore.MAGENTA + F'{"Add Book":^48}')
    book_id = len(read_book()) + 101
    print(Fore.BLUE + f'The Book Id is :: {book_id}')
    

    book_name = input(Fore.BLUE + "Enter The Book Name :: ")
    for i in read_book():
        if book_name.lower() in i.lower():
            print(Fore.RED + "The Book is Alredy exist")
            return()
        
    author_name = input(Fore.BLUE + "Enter the book author Name :: ")

    while True:
        quantity = input(Fore.BLUE + "Enter the Book Quantity :: ").strip()
        if quantity.isdigit():
            if int(quantity) > 0 :
                quantity = int(quantity)
                break
            else:
                print(Fore.RED + "Enter the valid Quentity")
            
        else:
            print(Fore.RED + f'{" Enter Valid Quantity":^48} \n {"Quntity cantain only no.":^48}')
    print(Fore.GREEN + f'{"Book Added Successfully":^48}')

    with open("books_info.txt", "a") as f:
        f.write(f"{book_id}, {book_name}, {author_name}, {quantity} \n")

    
def viwe_book():
    print(Fore.MAGENTA + F'{"Viwe Book":^48}')

    book_data = read_book()
    

    if len(read_book()) == 0:
            print(Fore.RED + 'There is no data about Book')
            
    else:

        for i in read_book():
            i = i.split()
            print(Fore.GREEN + f'Book Id : {i[0]} || Book Name : {i[1]} || Author Name : {i[2]} || Quentity : {i[-1]}')

search = ()
def search_book(search):
 
    print(Fore.MAGENTA + F'{"Search Book":^48}')
    #search = (input("Enter Book Id or Book Name :: "))
    search = input(Fore.BLUE + "Enter Book Id or Book Name :: ")
    book_data = read_book()
    if len(book_data) == 0:
        print(Fore.RED + "Sorry, No data in Book info ")
    else:
        if search.isdigit():
            
            for i in book_data:
                i = i.strip().split()
                if i[0]== search + ",":
                    print(Fore.GREEN + f'Book Id : {i[0]} || Book Name : {i[1]} || Author Name : {i[2]} || Quentity : {i[-1]}')
                    break
            else:
                    print(Fore.RED + "Sorry, The book id is not found")
                
        

        else:
            
            for i in book_data:
                i  = i.strip().split()
                if i[1].lower() == search.lower() + ",":
                    print(Fore.GREEN + f'Book Id : {i[0]} || Book Name : {i[1]} || Author Name : {i[2]} || Quentity : {i[-1]}')
                    break
                else:
                    print(Fore.RED + "Sorry, The book id is not found")


def resister_user():
    
    book_data = read_book()
   
    print(Fore.MAGENTA + F'{"Resister User":^48}')
    user_id = len(read_user()) + 1
    print(Fore.BLUE + f'The Resister Id is :: {user_id}')
   

    user_name = input(Fore.BLUE + "Enter The User Name :: ")
    for i in read_user():
        if user_name.lower() in i.lower():
            print(Fore.RED + "The user is Alredy exist")
            return()

    
   

    

    while True:
        mobail = input(Fore.BLUE + "Enter the Mobaile Number :: ")
        if mobail.isdigit():
            if len(mobail) == 10 :
                mobail = int(mobail)
                break
            else:
                print(Fore.RED + "Enter the valid Mobaile Number")
            
        else:
            print(Fore.RED + f'{" Enter Valid Mobaile Number":^48} \n {"Mobaile Number cantain only no.":^48}')
    print(Fore.GREEN + f'{"User Added Successfully":^48}')

    with open("user_info.txt", "a") as f:
        f.write(f"{user_id}, {user_name}, {mobail}, \n")


def issued_book():
    print(Fore.MAGENTA + F'{"Issued Book":^48}')
    book = input(Fore.BLUE + "Enter either Book name or Book id :: ")
    
    
    book_data =  read_book()
    user_data = read_user()
   
        
    if len(book_data) == 0:
        print(Fore.RED + "Sorry, No book are avilable for issued")

    else: 
        if book.isdigit():
            
            for i in book_data:
                i = i.strip().split()
                
                if i[0] == book + ",":
                    q = input(Fore.BLUE + "Enter requred Quntity :: " )
                                  
                    if int(i[-1]) >= int(q):                        
                        print(Fore.GREEN + "Your Request is accepted")
                        user = input(Fore.BLUE + "Enter user id :: ")
                        if len(user_data) == 0:
                            print(Fore.RED + "Sorry, No User are avilable for issued")
                        else:
                            for j in read_user():
                                j = j.strip().split()
                                if j[0] == user + ",":
                                    print(Fore.GREEN + "Isssued detail are added successfully")                                
                                    with open ("issued_info.txt", "a") as k:
                                        k.write(f"Book Id = {i[0]} ! Book name = {i[1]} is Issued to User id == {j[0]} ! Uesr name = {j[1]} ! in Quntity == {q}\n")
                                
                                    break
                            else:
                                print(Fore.RED + "Sorry, There is no user id is found")
                    else:
                            print(Fore.RED + f"sorry, we have only {i[-1]} books are avilable")
                    break
            else:
                print(Fore.RED + "Sorry, There is no book id is found!")
                    

                    


        else: 
            
                        
            for i in book_data:
                i = i.strip().split()
                
                if i[1].lower() == book.lower() + ",":
                    q = input(Fore.BLUE + "Enter requred Quntity :: " )
                                    
                    if int(i[-1]) >= int(q):                        
                        print(Fore.GREEN + "Your Request is accepted")
                        user = input(Fore.BLUE + "Enter user id :: ")
                        if len(user_data) == 0:
                            print(Fore.RED + "Sorry, No User are avilable for issued")
                        else:
                            for j in read_user():
                                j = j.strip().split()
                                if j[0] == user + ",":
                                    print(Fore.GREEN + "Isssued detail are added successfully")                                
                                    with open ("issued_info.txt", "a") as k:
                                        k.write(f"Book Id = {i[0]} ! Book name = {i[1]} is Issued to User id == {j[0]} ! Uesr name = {j[1]} ! in Quntity == {q}\n")                               
                                    break
                            else:
                                print(Fore.RED + "Sorry, There is no user id is found")
                    else:
                            print(Fore.RED + f"sorry, we have only {i[-1]} books are avilable")
                    break
            else:
                print(Fore.RED + "Sorry, There is no book id is found!")






                        
                




while True:
    menu()
    choise = input("Enter the Choise for Book in range 1 to 6 :: ")

    if choise <= "6":
        if choise == "1":
            add_book()
            
        elif choise == "2":
            viwe_book()
        elif choise == "3":
            search_book(search)
        elif choise == '4':
            resister_user()
        elif choise == '5':
            issued_book()
        else:
            print(Fore.CYAN +F'{"Thank You! Visit Again":^48}')
            break
    else:
        print(Fore.RED + f'{"Enter valid Choise":^48}')