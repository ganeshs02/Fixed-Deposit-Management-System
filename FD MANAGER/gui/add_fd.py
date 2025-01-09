# GUI for adding FDs

import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to insert FD into the database
def add_fd():
    bank_name = entry_bank_name.get()
    deposit_amount = entry_deposit_amount.get()
    start_date = entry_start_date.get()
    maturity_date = entry_maturity_date.get()
    interest_rate = entry_interest_rate.get()

    if not bank_name or not deposit_amount or not start_date or not maturity_date or not interest_rate:
        messagebox.showerror("Input Error", "All fields must be filled!")
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
window = tk.Tk()
window.title("Add Fixed Deposit")

# Creating labels and entry fields for user input
tk.Label(window, text="Bank Name").grid(row=0, column=0)
entry_bank_name = tk.Entry(window)
entry_bank_name.grid(row=0, column=1)

tk.Label(window, text="Deposit Amount").grid(row=1, column=0)
entry_deposit_amount = tk.Entry(window)
entry_deposit_amount.grid(row=1, column=1)

tk.Label(window, text="Start Date (YYYY-MM-DD)").grid(row=2, column=0)
entry_start_date = tk.Entry(window)
entry_start_date.grid(row=2, column=1)

tk.Label(window, text="Maturity Date (YYYY-MM-DD)").grid(row=3, column=0)
entry_maturity_date = tk.Entry(window)
entry_maturity_date.grid(row=3, column=1)

tk.Label(window, text="Interest Rate (%)").grid(row=4, column=0)
entry_interest_rate = tk.Entry(window)
entry_interest_rate.grid(row=4, column=1)

# Submit Button to add FD
button_add_fd = tk.Button(window, text="Add Fixed Deposit", command=add_fd)
button_add_fd.grid(row=5, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
