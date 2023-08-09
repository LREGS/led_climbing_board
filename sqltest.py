import sqlite3

cx = sqlite3.connect("testing.db")

cu = cx.cursor()

cu.execute("CREATE TABLE lang(name, first_appeared)")

cu.execute("INSERT INTO lang VALUES (?,?)", ("C", 1972))

for row in cu.execute("SELECT * from lang"):
    print(row)

cx.close