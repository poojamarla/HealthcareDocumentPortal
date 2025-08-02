import sqlite3

# Connect to the database (creates if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create the table
conn.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        filepath TEXT NOT NULL,
        filesize INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
''')

# Commit and close connection
conn.commit()
conn.close()

print("Database and table created successfully.")