def count_vowels(string):
   vowels = 'aeiouаеёиоуыэюя'
   return sum(1 for char in string.lower() if char in vowels)

# import sqlite3
#
# def init_db():
#    conn = sqlite3.connect(':memory:')
#    cursor = conn.cursor()
#    cursor.execute('''
#    CREATE TABLE IF NOT EXISTS users (
#    id INTEGER PRIMARY KEY,
#    name TEXT,
#    age INTEGER)
#    ''')
#    return conn
#
# def add_user(conn, name, age):
#    cursor = conn.cursor()
#    cursor.execute('''
#    INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
#    conn.commit()
#
# def get_user(conn, name):
#    cursor = conn.cursor()
#    cursor.execute('''SELECT * FROM users WHERE name=?''', (name,))
#    return cursor.fetchone()

# def sort_list(numbers):
#    return sorted(numbers)

# def is_palindrome(s):
#    return s == s[::-1]

# def check(number):
#    return number % 2 == 0

