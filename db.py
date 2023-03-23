import sqlite3
conn = sqlite3.connect(r'crm.db')
c = conn.cursor()
def insert_customer(first_name,last_name,address,phone,email,employee):
    conn = sqlite3.connect(r'crm.db')
    c = conn.cursor()
    sql=("INSERT INTO customer (first_name,last_name,address,phone,email,employee) VALUES(?,?,?,?,?,?)")
    val=(first_name.casefold(),last_name.casefold(),address,phone,email,employee)
    c.execute(sql,val)
    conn.commit()
    print("Data Entered successfully.")


def insert_user(email,password,name):
    sql = ("INSERT INTO user (email,password,name) VALUES(?,?,?)")
    val = (email,password,name.casefold())
    c.execute(sql, val)
    conn.commit()
    print("Data Entered successfully.")
def insert_inventory(product_name,price,quantity):
    conn = sqlite3.connect(r'crm.db')
    c = conn.cursor()
    sql=("INSERT INTO inventory (product_name,price,quantity) VALUES(?,?,?)")
    val=(product_name.casefold(),price,quantity)
    c.execute(sql,val)   
    conn.commit()
    print("Data Entered successfully.")

def update_inventory(id,data):
        sql = ("UPDATE inventory SET product_name=?,price=?,quantity=? WHERE id=?")
        val=(data[0],data[1],data[2],id,)
        c.execute(sql,val)
        myresult = c.fetchall()
        conn.commit()
        print("Update Inventory")
        return myresult


def update_customer(id,data):
    sql = "UPDATE customer SET first_name=?,last_name=?,address=?,phone=?,email=?,employee=? WHERE id=?"
    val = (data[0].casefold(),data[1].casefold(),data[2].casefold(),data[3].casefold(),data[4].casefold(),data[5].casefold(),id)
    c.execute(sql, val)
    myresult = c.fetchall()
    conn.commit()
    print("Update Customer")
    return myresult


def update_order(id,data):
    sql = "UPDATE order_ SET date=?,item_id=?,quantity=?,price=?,discount=? where id=?"
    val = (data[0],data[1].casefold(),data[2],data[3],data[4],id)
    c.execute(sql, val)
    conn.commit()
    print("Update order")
    return

def delete_customer(id):
    sql = "DELETE from customer where id=?"
    val = (id,)
    c.execute(sql, val)
    conn.commit()
    print("Deleted...")
    return

def delete_inventory(id):
    sql = "DELETE from inventory where id=?"
    val = (id,)
    c.execute(sql, val)
    conn.commit()
    print("Deleted...")
    return


def delete_order(id):
    sql = "DELETE from order_ where id=?"
    val = (id,)
    c.execute(sql, val)
    conn.commit()
    print("Deleted...")
    return


def insert_order(customer_name,date,order_item,quantity,price,discount):
    conn = sqlite3.connect(r'crm.db')
    c = conn.cursor()
    sql=("INSERT INTO order_ (customer_id,date,item_id,quantity,price,discount) VALUES(?,?,?,?,?,?)")
    val=(customer_name,date,order_item.casefold(),quantity,price,discount)
    c.execute(sql,val)
    myresult = c.fetchone()
    conn.commit()
    print("Data Entered successfully.")
    return myresult



def get_order(product_name):
        conn = sqlite3.connect(r'crm.db')
        c = conn.cursor()
        sql = ("SELECT quantity FROM inventory where product_name=?")
        val=(product_name,)
        c.execute(sql,val)
        myresult = c.fetchall()
        conn.commit()
        return myresult
# def get_order_data(product_name):
#         sql = ("SELECT * FROM order_ where product_name=?")
#         val=(product_name,)
#         c.execute(sql,val)
#         myresult = c.fetchall()
#         conn.commit()
#         return myresult
def get_inventory_data():
    conn = sqlite3.connect(r'crm.db')
    c = conn.cursor()

    sql = "SELECT * FROM inventory"
    c.execute(sql)
    myresult = c.fetchall()
    conn.commit()
    return myresult
def get_order_data(customer_name=None):
        conn = sqlite3.connect(r'crm.db')
        c = conn.cursor()
        if customer_name!=None:
            sql = "SELECT order_.id, customer.first_name, order_.date, order_.item_id, order_.quantity, order_.price,order_.discount from ORDER_ INNER JOIN customer on order_.customer_id = customer.id where customer.first_name=?"

            val=(customer_name,)
            c.execute(sql,val)
        else:
            sql = "SELECT order_.id, customer.first_name, order_.date, order_.item_id, order_.quantity, order_.price,order_.discount from ORDER_ INNER JOIN customer on order_.customer_id = customer.id"

            c.execute(sql)
        myresult = c.fetchall()
        conn.commit()
        return myresult


def get_customer_data(name=None):
    conn = sqlite3.connect(r'crm.db')
    c = conn.cursor()
    if name!=None:
        sql = "SELECT * FROM customer where first_name=?"
        val = (name,)
        c.execute(sql, val)
    else:
        sql= "SELECT * FROM customer"
        c.execute(sql)
    myresult = c.fetchall()
    conn.commit()
    return myresult

def log_in(email):

    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    sql = ("SELECT * FROM user where email=?")
    c.execute(sql,(email,))
    myresult = c.fetchall()
    conn.commit()
    return myresult
        

# def log_inset():
#     sql = ("INSERT INTO user (email, password) VALUES(?,?)")
#     val = ("sharjeel","1122")
#     c.execute(sql,val)
#     myresult = c.fetchall()
#     conn.commit()
#     print("Login successfully.")
# insert_user("admin","admin","admin")


def delete_schedule(id):
    sql = "DELETE from schedule_ where id=?"
    val = (id,)
    c.execute(sql, val)
    conn.commit()
    print("Deleted...")
    return


def insert_schedule(customer_name,title,date,time,duration):
    conn = sqlite3.connect(r'crm.db')
    c = conn.cursor()
    sql=("INSERT INTO schedule_ (customer_id,title,date,time,duration) VALUES(?,?,?,?,?)")
    val=(customer_name,title,date,time,duration)
    c.execute(sql,val)
    myresult = c.fetchone()
    conn.commit()
    print("Data Entered successfully.")
    return myresult


def update_schedule(id,data):
    sql = "UPDATE schedule_ SET title=?,date=?,time=?,duration=? where id=?"
    val = (data[0],data[1],data[2],data[3],id)
    c.execute(sql, val)
    conn.commit()
    print("Update order")
    return


def get_schedule(product_name):
    conn = sqlite3.connect(r'crm.db')
    c = conn.cursor()
    sql = ("SELECT quantity FROM inventory where product_name=?")
    val=(product_name,)
    c.execute(sql,val)
    myresult = c.fetchall()
    conn.commit()
    return myresult


def get_schedule_data(customer_name=None):
        conn = sqlite3.connect(r'crm.db')
        c = conn.cursor()
        if customer_name!=None:
            sql = "SELECT schedule_.id, customer.first_name, schedule_.title, schedule_.date, schedule_.time, schedule_.duration from SCHEDULE_ INNER JOIN customer on schedule_.customer_id = customer.id where customer.first_name=?"

            val=(customer_name,)
            c.execute(sql,val)
        else:
            sql = "SELECT schedule_.id, customer.first_name, schedule_.title, schedule_.date, schedule_.time, schedule_.duration from SCHEDULE_ INNER JOIN customer on schedule_.customer_id = customer.id"

            c.execute(sql)
        myresult = c.fetchall()
        conn.commit()
        return myresult