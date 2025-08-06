import sqlite3
from datetime import datetime

DB_NAME = "query_logs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp TEXT,
            raw_response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, raw_response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, timestamp, raw_response)
        VALUES (?, ?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, timestamp, raw_response))
    conn.commit()
    conn.close()
