# GUI for viewing/editing/deleting FDs

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def view_fds():
    try:
        # Correct path to the SQLite database file
        conn = sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db")
        cursor = conn.cursor()

        # Fetch all the fixed deposits
        cursor.execute("SELECT * FROM FixedDeposits")
        rows = cursor.fetchall()

        # Close the connection
        conn.close()

        # Clear the tree view before adding the new data
        for row in treeview.get_children():
            treeview.delete(row)

        # Insert rows into the table (treeview widget)
        for row in rows:
            treeview.insert("", "end", values=row)
    except sqlite3.DatabaseError as e:
        messagebox.showerror("Database Error", f"Error accessing the database: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the Tkinter window
window = tk.Tk()
window.title("View Fixed Deposits")

# Create a treeview widget to display the data  
columns = ("ID", "Bank Name", "Deposit Amount", "Start Date", "Maturity Date", "Interest Rate")
treeview = ttk.Treeview(window, columns=columns, show="headings")

# Set headings and column properties with center alignment
for col in columns:
    treeview.heading(col, text=col, anchor="center")  # Align the heading to center
    treeview.column(col, anchor="center", width=150)  # Align the data to center and set width

treeview.pack(fill=tk.BOTH, expand=True)

# Button to load data
button_view_fds = tk.Button(window, text="Load Fixed Deposits", command=view_fds)
button_view_fds.pack()

# Run the Tkinter event loop
window.mainloop()
