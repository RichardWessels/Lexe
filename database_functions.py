import sqlite3 as sql 

def create_connection(db_file):
    """ 
    create a database connection to the SQLite database
    specified by db_file
    
    db_file: database file
    returns: Connection object or None
    """
    conn = None
    try:
        conn = sql.connect(db_file)
    except sql.Error as e:
        print(e)
 
    return conn

def add_word(conn, word):
    sql = '''INSERT INTO words (word) VALUES (?, ?);'''

    cur = conn.cursor()
    cur.execute(sql, (word,))
    return cur.lastrowid

def find_word(conn, word):
    sql = '''SELECT * FROM words WHERE word=?;'''
    cur = conn.cursor()
    cur.execute(sql, (word,))
    row = cur.fetchone()
    return row

def delete_word(conn, word):
    sql = '''DELETE FROM words WHERE word=?;'''
    cur = conn.cursor()
    cur.execute(sql, (word,))

def return_list(conn):
    sql = '''SELECT * FROM words;'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows
