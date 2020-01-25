import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("books.db")
        self.cur = con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
        self.con.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
        self.con.commit()

    def viewall(self):
        self.cur.execute("SELECT * FROM book")
        self.rows = cur.fetchall()
        return rows


    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ",(title, author, year, isbn))
        self.rows = cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id= ?", (id,))
        self.con.commit()


    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id= ?", (title, author, year, isbn, id))
        self.con.commit()

    def close():
        self.con.close()


#connect()
#insert("animal farm","george orwell", 1984, 007)
#rows= search(title="animal farm")
#print rows
