import sqlite3


def show_menu():
    print("1- show list")
    print("2- add new")
    print("3- edit")
    print("4- remove")

def load_database():
    global con, cursor
    con= sqlite3.connect("chinook.db")
    cursor= con.cursor()

def show_list():
    for data in cursor.execute("SELECT * FROM customers WHERE Country='Germany'"):
        print(data)

    result = cursor.execute("SELECT * FROM genres")
    customers= result.fetchall()
    for customer in customers:
        print(customer)

def add_new():

    new_genre_name = input("enter a name for your new genre: ")
    cursor.execute(f'INSERT INTO genres(Name) VALUES("{new_genre_name}")')
    con.commit()


def edit():
    new_country = input("enter country name: ")
    new_city = input("enter city name: ")
    firstname_customer = input("enter first name: ")
    cursor.execute(f"UPDATE customers SET Country='{new_country}',City='{new_city}' WHERE FirstName='{firstname_customer}'")
    #cursor.execute(f"UPDATE customers SET Country='{new_country}',City='{new_city}' WHERE FirstName='kara' AND CustomerId=9")
    con.commit()
    

def remove():
    genre_name= input("enter genre name: ")
    cursor.execute(f"DELETE FROM genres WHERE Name='{genre_name}'")
    con.commit()




load_database()
while True:
    show_menu()
    choice = int(input())
    if choice == 1:
        show_list()
    elif choice == 2:
        add_new()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()