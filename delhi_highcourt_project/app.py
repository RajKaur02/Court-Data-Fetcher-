from flask import Flask, request, jsonify, render_template, send_file
from case_scraper import fetch_case_details
import sqlite3
import csv
import pandas as pd
from io import BytesIO, StringIO
import webbrowser
import threading
import time
import os

app = Flask(__name__)

# --- DB Init ---
def init_db():
    conn = sqlite3.connect("db_logger.db")
    cursor = conn.cursor()
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

def log_to_db(case_type, case_number, filing_year, raw_response):
    conn = sqlite3.connect("db_logger.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, raw_response)
        VALUES (?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, raw_response))
    conn.commit()
    conn.close()

init_db()

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form.get('case_type')
    case_number = request.form.get('case_number')
    case_year = request.form.get('case_year')
    result = fetch_case_details(case_type, case_number, case_year)
    log_to_db(case_type, case_number, case_year, str(result))
    return jsonify(result)

@app.route('/download/csv')
def download_csv():
    conn = sqlite3.connect("db_logger.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM queries ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    output_str = StringIO()
    writer = csv.writer(output_str)
    writer.writerow(['ID', 'Case Type', 'Case Number', 'Filing Year', 'Query Time', 'Raw Response'])
    writer.writerows(rows)

    output_bytes = BytesIO()
    output_bytes.write(output_str.getvalue().encode('utf-8'))
    output_bytes.seek(0)

    return send_file(
        output_bytes,
        mimetype='text/csv',
        as_attachment=True,
        download_name='case_queries.csv'
    )

@app.route('/download/excel')
def download_excel():
    conn = sqlite3.connect("db_logger.db")
    df = pd.read_sql_query("SELECT * FROM queries ORDER BY id DESC", conn)
    conn.close()

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Case Queries')
    output.seek(0)

    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='case_queries.xlsx'
    )

# --- Auto Open Browser + Start Server ---
def open_browser():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:5000/')



if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':  # This only runs on the final load
        # Only open browser or run Selenium code here
        pass  # (Your browser opening logic here)
    app.run(debug=True)

