import sqlite3
import tkinter as tk
from tkinter import messagebox
from utils.validation import validate_bank_name, validate_deposit_amount, validate_dates  # Import validation functions

# Function to load data for editing
def load_fd_details():
    fd_id = entry_fd_id.get()

    if not fd_id.isdigit():
        messagebox.showerror("Input Error", "FD ID must be a valid number!")
        return

    # Fetch the record from the database
    conn = sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FixedDeposits WHERE id=?", (fd_id,))
    record = cursor.fetchone()
    conn.close()

    if record:
        # Fill the fields with current data
        entry_bank_name.delete(0, tk.END)
        entry_bank_name.insert(0, record[1])
        entry_deposit_amount.delete(0, tk.END)
        entry_deposit_amount.insert(0, record[2])
        entry_start_date.delete(0, tk.END)
        entry_start_date.insert(0, record[3])
        entry_maturity_date.delete(0, tk.END)
        entry_maturity_date.insert(0, record[4])
        entry_interest_rate.delete(0, tk.END)
        entry_interest_rate.insert(0, record[5])
    else:
        messagebox.showerror("Error", "FD ID not found!")

# Function to save edited data
def save_fd_details():
    fd_id = entry_fd_id.get()
    bank_name = entry_bank_name.get()
    deposit_amount = entry_deposit_amount.get()
    start_date = entry_start_date.get()
    maturity_date = entry_maturity_date.get()
    interest_rate = entry_interest_rate.get()

    # Validate inputs
    if not validate_bank_name(bank_name):
        messagebox.showerror("Input Error", "Invalid bank name!")
        return
    if not validate_deposit_amount(deposit_amount):
        messagebox.showerror("Input Error", "Deposit amount must be a positive number!")
        return
    if not validate_deposit_amount(interest_rate):
        messagebox.showerror("Input Error", "Interest rate must be a positive number!")
        return
    if not validate_dates(start_date, maturity_date):
        messagebox.showerror("Input Error", "Invalid dates or maturity date is earlier than start date!")
        return

    # Update the database record
    conn = sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db")
    cursor = conn.cursor()
    query = """
    UPDATE FixedDeposits
    SET bank_name=?, deposit_amount=?, start_date=?, maturity_date=?, interest_rate=?
    WHERE id=?;
    """
    cursor.execute(query, (bank_name, deposit_amount, start_date, maturity_date, interest_rate, fd_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Fixed Deposit details updated successfully!")

# Tkinter GUI setup
window = tk.Tk()
window.title("Edit Fixed Deposit")

# Input fields for editing
tk.Label(window, text="FD ID").grid(row=0, column=0)
entry_fd_id = tk.Entry(window)
entry_fd_id.grid(row=0, column=1)

tk.Label(window, text="Bank Name").grid(row=1, column=0)
entry_bank_name = tk.Entry(window)
entry_bank_name.grid(row=1, column=1)

tk.Label(window, text="Deposit Amount").grid(row=2, column=0)
entry_deposit_amount = tk.Entry(window)
entry_deposit_amount.grid(row=2, column=1)

tk.Label(window, text="Start Date (YYYY-MM-DD)").grid(row=3, column=0)
entry_start_date = tk.Entry(window)
entry_start_date.grid(row=3, column=1)

tk.Label(window, text="Maturity Date (YYYY-MM-DD)").grid(row=4, column=0)
entry_maturity_date = tk.Entry(window)
entry_maturity_date.grid(row=4, column=1)

tk.Label(window, text="Interest Rate (%)").grid(row=5, column=0)
entry_interest_rate = tk.Entry(window)
entry_interest_rate.grid(row=5, column=1)

# Buttons for actions
tk.Button(window, text="Load Details", command=load_fd_details).grid(row=6, column=0, columnspan=2)
tk.Button(window, text="Save Changes", command=save_fd_details).grid(row=7, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
