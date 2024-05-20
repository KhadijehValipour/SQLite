import sqlite3


def show_menu():
    print("1-show list genres")
    print("2-add new")
    print("3-edit")
    print("4-remove")
    print("5-show list customers")


def load_database():
    global connection
    global my_cursor
    connection = sqlite3.connect("chinook.db")
    my_cursor = connection.cursor()


def show_list_genres():
    # for data in my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'"):
    #     print(data)

    result = my_cursor.execute("SELECT * FROM genres")
    Genres = result.fetchall()
    for genre in Genres:
        print(genre)


def show_list_customers():
    result = my_cursor.execute("SELECT * FROM customers")
    Customers = result.fetchall()
    for customer in Customers:
        print(customer)


def add_new():
     new_genre_name = input("enter a name for your new genre: ")
     my_cursor.execute(f"INSERT INTO genres(Name) VALUES('{new_genre_name}')")
     connection.commit()

def edit():
    new_city = input("enter a new city: ")
    new_country = input("enter a new country: ")
    name = input("enter a customer name: ")
    id = int(input("enter a customer id :"))

    my_cursor.execute(f"UPDATE customers SET City='{new_city}', Country='{new_country}' WHERE FirstName='{name}' AND CustomerId={id}")
    connection.commit()


def remove():
    genre_name = input("enter a genre name :")
    my_cursor.execute(f"DELETE FROM genres WHERE Name='{genre_name}'")
    print(f"{genre_name} has been successfully uninstalled")
    connection.commit()



load_database()

while True:
    show_menu()
    choice = int(input())

    if choice == 1:
        show_list_genres()
    elif choice == 2:
        add_new()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()
    elif choice == 5:
        show_list_customers()