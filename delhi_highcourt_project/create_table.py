import sqlite3

# Connect to the database file
conn = sqlite3.connect("db_logger.db")
cursor = conn.cursor()

# Create the 'queries' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_type TEXT,
        case_number TEXT,
        filing_year TEXT,
        query_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        raw_response TEXT
    )
''')

conn.commit()
conn.close()

print(" Table 'queries' created successfully!")
