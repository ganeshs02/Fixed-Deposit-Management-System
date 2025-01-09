import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to fetch the FD record by ID
def fetch_record(id):
    try:
        with sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM FixedDeposits WHERE id = ?", (id,))
            record = cursor.fetchone()
        return record
    except sqlite3.DatabaseError as e:
        messagebox.showerror("Database Error", f"Error accessing the database: {e}")
        return None

# Function to delete the record after confirmation
def delete_record(id):
    try:
        with sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM FixedDeposits WHERE id = ?", (id,))
            conn.commit()
        messagebox.showinfo("Success", f"Record with ID {id} has been deleted.")
        load_data()  # Refresh the data
    except sqlite3.DatabaseError as e:
        messagebox.showerror("Database Error", f"Error deleting the record: {e}")

# Function to load all the records from the database and update the treeview
def load_data():
    try:
        # Clear the treeview before loading new data
        for row in treeview.get_children():
            treeview.delete(row)
        
        with sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM FixedDeposits")
            records = cursor.fetchall()

        # Insert records into the treeview
        for record in records:
            treeview.insert("", "end", values=record)
    except sqlite3.DatabaseError as e:
        messagebox.showerror("Database Error", f"Error accessing the database: {e}")

# Function to handle the remove action (view and confirm)
def remove_fd():
    id = entry_id.get()

    # Validate ID (ensure it's an integer and not empty)
    if not id.isdigit() or id == "":
        messagebox.showerror("Error", "Please enter a valid ID.")
        return

    # Convert the ID to integer
    id = int(id)

    # Check that the ID is greater than 0
    if id <= 0:
        messagebox.showerror("Error", "Please enter a valid ID greater than 0.")
        return

    # Fetch the record to be deleted
    record = fetch_record(id)

    if record:
        # Display the record details for confirmation
        record_details = f"ID: {record[0]}\nBank Name: {record[1]}\nDeposit Amount: {record[2]}\nStart Date: {record[3]}\nMaturity Date: {record[4]}\nInterest Rate: {record[5]}"
        
        # Ask for confirmation before deleting
        confirm = messagebox.askyesno("Delete Record", f"Are you sure you want to delete this record?\n\n{record_details}")
        
        if confirm:
            delete_record(id)
    else:
        messagebox.showerror("Error", "Record not found. Please make sure the ID exists.")

# Setting up the Tkinter window (optional for user interface)
window = tk.Tk()
window.title("Remove Fixed Deposit")

# Create the Treeview widget to display the records (optional for displaying the FD list)
columns = ("ID", "Bank Name", "Deposit Amount", "Start Date", "Maturity Date", "Interest Rate")
treeview = ttk.Treeview(window, columns=columns, show="headings")

# Set headings and column properties
for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, width=150)  # Adjust column width as needed

treeview.pack(fill=tk.BOTH, expand=True)

# Add input field for entering ID
label_id = tk.Label(window, text="Enter FD ID to remove:")
label_id.pack()

entry_id = tk.Entry(window)
entry_id.pack()

# Add a button to trigger the removal process
button_remove = tk.Button(window, text="Remove FD", command=remove_fd)
button_remove.pack()

# Load data to show existing records
load_data()

# Run the Tkinter event loop
window.mainloop()
