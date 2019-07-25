import sqlite3

def createtab():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(Item NOT NULL TEXT PRIMARY KEY,Quantity INTEGER,Price REAL)")
    conn.commit()
    conn.close()

def insert_item(name,qnty,pr):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(name,qnty,pr))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    row=conn.fetchall()
    conn.close
    return row
print(view())

def delete():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE Item=?",(item))
    conn.commit()
    conn.close
delete(pencil)
print(view())

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item) )
    conn.commit()
    conn.close
    print(view())
