import sqlite3

def add_flavor(name, is_seasonal):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute("INSERT INTO flavors (name, is_seasonal) VALUES (?, ?)", (name, is_seasonal))
    conn.commit()
    conn.close()

def add_ingredient(name, quantity):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()

def add_allergen(name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute("INSERT INTO allergens (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def add_customer_suggestion(flavor_name, customer_name, allergy_concerns):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute("INSERT INTO customer_suggestions (flavor_name, customer_name, allergy_concerns) VALUES (?, ?, ?)",
              (flavor_name, customer_name, allergy_concerns))
    conn.commit()
    conn.close()

def add_to_cart(flavor_id):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute("INSERT INTO cart (flavor_id) VALUES (?)", (flavor_id,))
    conn.commit()
    conn.close()

def get_flavors():
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute("SELECT * FROM flavors")
    flavors = c.fetchall()
    conn.close()
    return flavors

def search_flavors(keyword):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute("SELECT * FROM flavors WHERE name LIKE ?", ('%' + keyword + '%',))
    flavors = c.fetchall()
    conn.close()
    return flavors
