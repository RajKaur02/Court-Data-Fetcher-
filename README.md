# Delhi High Court Case Status Scraper (Flask + Selenium + SQLite)

Python web app to retrieve **Delhi High Court Case Details** with **Flask**, **Selenium WebDriver**, and stores search queries in an **SQLite database**. Users can submit case details through a web form and extract case status directly from the official Delhi High Court website.

---

## Features
- Input **Case Type, Case Number, Case Year** via easy web interface.
- Submits forms on Delhi High Court website automatically with **Selenium WebDriver**.
- Supports Manual Captcha solving.
- Results in a nicely formatted Case Status table.
- Logs all search queries into an **SQLite Database**.
- Download Query Logs as **CSV** or **Excel** file from the interface itself.

---

## Project Structure
delhi-court-project/
├── app.py # Flask backend and API routes

├── case_scraper.py # Selenium automation script

├── create_table.py # Script to create 'queries' table in DB

├── db_logger.py # Handles logging of user queries into SQLite DB

├── view_db.py # View logged queries from DB

├── query_logs.db # SQLite database file for logging(automatic gn.)

├── templates/
│ └── index.html # Frontend form UI

├── static/ # (Optional: CSS/JS files)

├── requirements.txt # Python dependencies

└── README.md # Project documentation


---
## Installation & Setup
 1. Clone the Repository:
```bash
git clone https://github.com/your-username/delhi-court-project.git
cd delhi-court-project
2. Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Initialize the Database:
bash
Copy
Edit
python create_table.py
▶️ Running the Application
bash
Copy
Edit
python app.py
Usage:
Open browser at: http://127.0.0.1:5000/

Fill in Case Type, Case Number, Case Year.

Click Fetch Case Details.

A browser window will open — Solve Captcha manually.

Case details will be fetched and shown on the page.

You can download the query logs as CSV or Excel.

???? Download Logs as CSV or Excel
Download CSV: Click the Download CSV button on the page.

Download Excel: Press the Download Excel button on the page.

Both operations will export query logs from query_logs.db → queries table.


????️ Technologies Used
Python 3.x
Flask
Selenium WebDriver
SQLite
Pandas & XlsxWriter (for CSV/Excel export)
HTML/CSS (Frontend)

???? Demo Video

Click the image above to view the demo.

???? Acknowledgements
Flask
Selenium WebDriver
webdriver-manager
Pandas
Delhi High Court Website for data access.


???? E-mail

nav191719@gmail.com
