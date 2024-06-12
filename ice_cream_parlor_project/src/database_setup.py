import sqlite3


def setup_database():
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS flavors (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 is_seasonal BOOLEAN)''')

    c.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 quantity INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS allergens (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 flavor_name TEXT,
                 customer_name TEXT,
                 allergy_concerns TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS cart (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 flavor_id INTEGER)''')

    conn.commit()
    conn.close()


setup_database()
