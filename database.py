import sqlite3

conn = sqlite3.connect('crm.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS user
          ([id] INTEGER PRIMARY KEY, [email] TEXT, [password] TEXT, [name] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS customer
          ([id] INTEGER PRIMARY KEY, [first_name] TEXT, [last_name] TEXT, [address] TEXT, [phone] TEXT,[email] TEXT, [employee] TEXT)
          ''')
          
c.execute('''
          CREATE TABLE IF NOT EXISTS inventory
          ([id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] TEXT, [quantity] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS order_
          ([id] INTEGER PRIMARY KEY, [customer_id] INTEGER, [date] TEXT, [item_id] INTEGER, [quantity] TEXT, [price] INTEGER, [discount] TEXT,FOREIGN KEY (customer_id)
       REFERENCES customer (id),FOREIGN KEY (item_id) REFERENCES inventory (id))
          ''')
                     
conn.commit()