import sqlite3
from tabulate import tabulate
from colorama import Fore, Back, Style
connection = sqlite3.connect('products.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL DEFAULT 0.00, available BOOLEAN DEFAULT 1)")
connection.commit()


def add_product(name, price):
    try:
        cursor.execute("INSERT INTO products(name,price) VALUES ('{}', {})".format(
        name, float(price)))
    except ValueError:
        print("Price must be a number")
    print(
        f"{Back.GREEN}{Fore.WHITE}[ACTION_ADD]{Style.RESET_ALL} Added new product with properties (name: {name}; price: {price})")


def del_product(id):
    try:
        cursor.execute("DELETE FROM products WHERE id = {}".format(id))
    except ValueError:
        print("ID must be a number")
    print(
        f"{Back.RED}{Fore.WHITE}[ACTION_DEL]{Style.RESET_ALL} Deleted product with id {id}")


def upd_product(id, name, price, available):
    try:
        cursor.execute("UPDATE products SET name = '{}', price = {}, available = {} WHERE id = {}".format(
        name, price, available, id))
    except ValueError:
        print("Price must be a number")
    print(
        f"{Back.YELLOW}{Fore.WHITE}[ACTION_UPD]{Style.RESET_ALL} Updated product with id {id} with properties (name: {name}; price: {price}; available: {available})")


def all_products():
    products = cursor.execute("SELECT * FROM products").fetchall()
    print(tabulate([list(i) for i in products], tablefmt="fancy_grid"))


# while True:
#     print(
#         f"{Back.BLUE}{Fore.WHITE}[MENU]{Style.RESET_ALL} 1. Add product; 2. Delete product; 3. Update product; 4. List Products; 5. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         add_product(input("Enter product name: "),
#                     input("Enter product price: "))
#     elif choice == 2:
#         del_product(int(input("Enter product id: ")))
#     elif choice == 3:
#         upd_product(int(input("Enter product id: ")), input("Enter product name: "), input(
#             "Enter product price: "), input("Enter product availability: "))
#     elif choice == 4:
#         all_products()
#     elif choice == 5:
#         break
#     else:
#         print(f"{Back.RED}{Fore.WHITE}[ERROR]{Style.RESET_ALL} Invalid choice")
#     connection.commit()


connection.close()
