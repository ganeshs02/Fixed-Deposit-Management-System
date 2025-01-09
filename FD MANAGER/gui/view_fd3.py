import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to view FDs from the database
def view_fds(treeview):
    try:
        # Correct path to the SQLite database file
        conn = sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db")
        cursor = conn.cursor()

        # Fetch all the fixed deposits
        cursor.execute("SELECT * FROM FixedDeposits")
        rows = cursor.fetchall()

        # Close the connection
        conn.close()

        # Clear the treeview before adding the new data
        for row in treeview.get_children():
            treeview.delete(row)

        # Check if there are rows in the database
        if not rows:
            messagebox.showinfo("No Records", "No Fixed Deposits found in the database.")
            return

        # Insert rows into the table (treeview widget)
        for row in rows:
            treeview.insert("", "end", values=row)

    except sqlite3.OperationalError as e:
        messagebox.showerror("Database Error", "The 'FixedDeposits' table does not exist in the database.")
    except sqlite3.DatabaseError as e:
        messagebox.showerror("Database Error", f"Error accessing the database: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the Tkinter window
def open_view_fd_window(window):
    # Create a new window for viewing Fixed Deposits
    view_window = tk.Toplevel(window)
    view_window.title("View Fixed Deposits")

    # Create a treeview widget to display the data  
    columns = ("ID", "Bank Name", "Deposit Amount", "Start Date", "Maturity Date", "Interest Rate")
    treeview = ttk.Treeview(view_window, columns=columns, show="headings")

    # Set headings and column properties with center alignment
    for col in columns:
        treeview.heading(col, text=col, anchor="center")  # Align the heading to center
        treeview.column(col, anchor="center", width=150)  # Align the data to center and set width

    treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Button to load data
    button_view_fds = tk.Button(view_window, text="Load Fixed Deposits", command=lambda: view_fds(treeview))
    button_view_fds.pack(pady=5)

    # Run the Tkinter event loop
    view_window.mainloop()

# Ensure this file only runs when executed directly
if __name__ == "__main__":
    open_view_fd_window(None)
