import sqlite3
import tkinter as tk
from tkinter import messagebox
from utils.validation import validate_bank_name, validate_deposit_amount, validate_dates, validate_interest_rate

# Function to insert FD into the database
def add_fd(entry_bank_name, entry_deposit_amount, entry_start_date, entry_maturity_date, entry_interest_rate):
    bank_name = entry_bank_name.get()
    deposit_amount = entry_deposit_amount.get()
    start_date = entry_start_date.get()
    maturity_date = entry_maturity_date.get()
    interest_rate = entry_interest_rate.get()

    # Validate the inputs
    if not validate_bank_name(bank_name):
        messagebox.showerror("Input Error", "Bank Name must not be empty and should only contain alphabets and spaces!")
        return

    if not validate_deposit_amount(deposit_amount):
        messagebox.showerror("Input Error", "Deposit Amount must be a positive number!")
        return

    if not validate_dates(start_date, maturity_date):
        messagebox.showerror("Input Error", "Start Date and Maturity Date must be in the format YYYY-MM-DD, and Maturity Date must be after Start Date!")
        return

    if not validate_interest_rate(interest_rate):
        messagebox.showerror("Input Error", "Interest Rate must be a positive number!")
        return

    # Insert into the database
    conn = sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db")
    cursor = conn.cursor()
    query = """
    INSERT INTO FixedDeposits (bank_name, deposit_amount, start_date, maturity_date, interest_rate)
    VALUES (?, ?, ?, ?, ?);   
    """
    data = (bank_name, deposit_amount, start_date, maturity_date, interest_rate)
    cursor.execute(query, data)
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Fixed Deposit added successfully!")

# Setting up the Tkinter window
def open_add_fd_window(window):
    # Creating a new window for adding a Fixed Deposit
    add_fd_window = tk.Toplevel(window)
    add_fd_window.title("Add Fixed Deposit")

    # Creating labels and entry fields for user input
    tk.Label(add_fd_window, text="Bank Name").grid(row=0, column=0)
    entry_bank_name = tk.Entry(add_fd_window)
    entry_bank_name.grid(row=0, column=1)

    tk.Label(add_fd_window, text="Deposit Amount").grid(row=1, column=0)
    entry_deposit_amount = tk.Entry(add_fd_window)
    entry_deposit_amount.grid(row=1, column=1)

    tk.Label(add_fd_window, text="Start Date (YYYY-MM-DD)").grid(row=2, column=0)
    entry_start_date = tk.Entry(add_fd_window)
    entry_start_date.grid(row=2, column=1)

    tk.Label(add_fd_window, text="Maturity Date (YYYY-MM-DD)").grid(row=3, column=0)
    entry_maturity_date = tk.Entry(add_fd_window)
    entry_maturity_date.grid(row=3, column=1)

    tk.Label(add_fd_window, text="Interest Rate (%)").grid(row=4, column=0)
    entry_interest_rate = tk.Entry(add_fd_window)
    entry_interest_rate.grid(row=4, column=1)

    # Submit Button to add FD
    button_add_fd = tk.Button(add_fd_window, text="Add Fixed Deposit", command=lambda: add_fd(entry_bank_name, entry_deposit_amount, entry_start_date, entry_maturity_date, entry_interest_rate))
    button_add_fd.grid(row=5, column=0, columnspan=2)

    # Run the Tkinter event loop for the add FD window
    add_fd_window.mainloop()

# Ensure this file only runs when executed directly
if __name__ == "__main__":
    window = tk.Tk()  # Main window instance
    window.title("FD Management System")
    
    # Example button in the main window to trigger add FD window
    add_fd_button = tk.Button(window, text="Add Fixed Deposit", command=lambda: open_add_fd_window(window))
    add_fd_button.pack()
    
    window.mainloop()
