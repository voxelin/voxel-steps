import sqlite3
from tabulate import tabulate
from colorama import Fore, Back, Style
connection = sqlite3.connect("workers.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS workers (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, age INTEGER, salary REAL)")


def create_user(name, surname, age, salary):
    cursor.execute('INSERT INTO workers(name, surname, age, salary) VALUES ("{}", "{}", {}, {})'.format(
        name, surname, age, salary))
    connection.commit()
    print(
        f'{Fore.WHITE}{Back.GREEN}[INFO]{Style.RESET_ALL}{Style.BRIGHT} Successfuly added a worker into workers.db {Style.RESET_ALL}{Fore.WHITE}{Back.GREEN}[ENDINFO]{Style.RESET_ALL}')

def get_users_above(salary):
    workers = cursor.execute('SELECT * FROM workers WHERE salary > {}'.format(salary)).fetchall()
    print(tabulate([list(i) for i in workers], tablefmt="fancy_grid"))
get_users_above(int(input("Enter salary [Format: 2000]: ")))
connection.close()