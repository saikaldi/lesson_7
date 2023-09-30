import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn
connection = create_connection('hw.db')

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

sql_create_products_table='''
    CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_title VARCHAR(200) NOT NULL,
    price NUMERIC(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

def insert_product(conn, product):
    sql='''INSERT INTO products(product_title, price,quantity)
    VALUES(?,?,?)'''
    try:
        cursor=conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def update_quantity(conn, product):
    sql='''UPDATE products SET quantity=? WHERE id=?'''
    try:
        cursor=conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def change_price(conn, product):
    sql='''UPDATE products SET price=? WHERE id=?'''
    try:
        cursor=conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    sql='''DELETE FROM products 
    WHERE id=?'''
    try:
        cursor=conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_product(conn):
    sql='''SELECT * FROM products '''
    try:
        cursor=conn.cursor()
        cursor.execute(sql)

        rows_list=cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
def select_all_produc_by_price_and_quatity(conn):
    sql = '''SELECT * FROM products WHERE price < 100.0 AND quantity > 5'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_products_by_title(conn, search_term):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    search_term = f"%{search_term}%"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (search_term,))

        rows_list = cursor.fetchall()
        if len(rows_list) > 0:
            print(f"Products matching '{search_term}':")
            for row in rows_list:
                print(row)
        else:
            print(f"No products found matching '{search_term}'.")
    except sqlite3.Error as e:
        print(e)


if connection is not None:
    # Create and connect to the database
    print('Successfully connected to the database!')
    # insert_product(connection, ('biscuit',10.99, 100))
    # insert_product(connection, ('apple', 0.99, 50))
    # insert_product(connection, ('banana', 0.49, 75))
    # insert_product(connection, ('orange', 0.79, 60))
    # insert_product(connection, ('spaghetti', 1.99, 40))
    # insert_product(connection, ('chicken breast', 4.99, 30))
    # insert_product(connection, ('rice', 2.49, 100))
    # insert_product(connection, ('eggs', 1.29, 90))
    # insert_product(connection, ('milk', 2.49, 80))
    # insert_product(connection, ('bread', 1.79, 70))
    # insert_product(connection, ('cheese', 3.99, 50))
    # insert_product(connection, ('lettuce', 1.29, 120))
    # insert_product(connection, ('carrots', 0.79, 100))
    # insert_product(connection, ('yogurt', 1.99, 60))
    # insert_product(connection, ('potato chips', 2.99, 45))
    # create_table(connection, sql_create_products_table)
    # connection = create_connection('hw.db')
    # update_quantity(connection, (2, 2))
    # change_price(connection, (200.99, 13))
    # delete_product(connection, 5)
    # select_all_product(connection)
    # select_all_produc_by_price_and_quatity(connection)
    # search_products_by_title(connection, 'carrot')
    connection.close()
else:
    print('Connection to the database failed.')