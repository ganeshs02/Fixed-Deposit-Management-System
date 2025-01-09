import tkinter as tk
from gui.add_fd3 import open_add_fd_window
from gui.view_fd3 import open_view_fd_window
from gui.remove_fd3 import open_remove_fd_window
from gui.edit_fd3 import open_edit_fd_window
from gui.reminders2 import check_and_send_reminders  # Adjusted path

# Tkinter main window setup
def main_window():
    window = tk.Tk()
    window.title("Fixed Deposit Management System")
    window.geometry("400x400")
    window.config(bg="#2c3e50")  # Dark blue background color

    window_width = 400
    window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Button styling for modern, professional look
    button_style = {
        'width': 30,
        'height': 2,
        'font': ("Helvetica", 12, "bold"),
        'fg': "white",
        'bg': "#16a085",  # Teal green color
        'activebackground': "#1abc9c",  # Lighter teal green on hover
        'bd': 0,  # Remove border
        'relief': "flat",  # No border relief
        'cursor': "hand2"  # Hand cursor on hover
    }

    # Add Fixed Deposit button
    
    add_fd_button = tk.Button(window, text="Add Fixed Deposit", **button_style, command=lambda: open_add_fd_window(window))
    add_fd_button.pack(pady=15)

    # View Fixed Deposits button
    view_fds_button = tk.Button(window, text="View Fixed Deposits", **button_style, command=lambda: open_view_fd_window(window))
    view_fds_button.pack(pady=15)

    # Remove Fixed Deposit button
    remove_fd_button = tk.Button(window, text="Remove Fixed Deposit", **button_style, command=lambda: open_remove_fd_window(window))
    remove_fd_button.pack(pady=15)

    # Edit Fixed Deposit button
    edit_fd_button = tk.Button(window, text="Edit Fixed Deposit", **button_style, command=open_edit_fd_window)
    edit_fd_button.pack(pady=15)
    
    # Send Reminders button
    reminders_button = tk.Button(window, text="Send Reminders", **button_style, command=check_and_send_reminders)
    reminders_button.pack(pady=15)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main_window()
