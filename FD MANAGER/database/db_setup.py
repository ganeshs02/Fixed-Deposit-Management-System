import sqlite3
import os

def setup_database():
    # Get the absolute path to the database folder
    db_folder = os.path.join(os.path.dirname(__file__))  # Adjust if needed
    db_path = os.path.join(db_folder, "fd_manager.db")
    print(f"Database will be created at: {db_path}")  # Debugging

    # Ensure the folder exists
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    # Connect to the database
    try:
        conn = sqlite3.connect(db_path)
        print("Database connection successful!")
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
        return

    # Create a cursor object
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FixedDeposits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bank_name TEXT NOT NULL,
            deposit_amount REAL NOT NULL,
            start_date TEXT NOT NULL,
            maturity_date TEXT NOT NULL,
            interest_rate REAL NOT NULL
        )
    """)

    # Commit and close
    conn.commit()
    conn.close()

    print("Database setup complete!")

if __name__ == "__main__":
    setup_database()
