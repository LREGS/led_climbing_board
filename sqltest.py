import sqlite3

from configuration import Configuartion

cx = sqlite3.connect("testing.db")

cu = cx.cursor()

cu.execute("CREATE TABLE IF NOT EXISTS lang(name, first_appeared)")

cu.execute("INSERT INTO lang VALUES (?,?)", ("C", 1972))

for row in cu.execute("SELECT NAME from lang"):
    print(row)

cx.close

# database = Configuartion()

# addusers = database.add_users()

# users = database.get_users()
