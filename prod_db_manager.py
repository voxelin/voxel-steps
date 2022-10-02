import sqlite3

conn = sqlite3.connect('products.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')

def add_product(name, price):
    c.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
    conn.commit()

def get_products():
    c.execute('''SELECT * FROM products''')
    return c.fetchall()

def delete_product(id):
    c.execute('''DELETE FROM products WHERE id=?''', (id,))
    conn.commit()

print("Welcome to the product manager!")
while True:
    print("1 - Add a product")
    print("2 - List all products")
    print("3 - Delete a product")
    print("4 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        name = input("Name: ")
        price = float(input("Price: "))
        add_product(name, price)
    elif option == "2":
        products = get_products()
        for product in products:
            print(product)
    elif option == "3":
        id = int(input("ID: "))
        delete_product(id)
    elif option == "4":
        break
    else:
        print("Invalid option!")
conn.commit()
conn.close()