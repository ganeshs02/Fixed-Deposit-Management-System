import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
import datetime
import re

# Email Setup - Update these values
sender_email = "ganeshsurle21@gmail.com"  # Your Gmail address
app_password = "cmmnvzenqijebkrx"  # The 16-character app password you got from Google
receiver_email = "ganeshsurle6@gmail.com"  # Receiver's email address (can be the same as sender)

# Email Validation
def validate_email_format(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Date Validation
def validate_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Database connection to fetch FD records
def get_upcoming_fds():
    conn = sqlite3.connect(r"C:\Users\Ganseh\Desktop\FD REM SYS\FD MANAGER\database\fd_manager.db")
    cursor = conn.cursor()
    
    # Get the current date and the date 2 days ahead
    current_date = datetime.datetime.now()
    reminder_date = current_date + datetime.timedelta(days=2)
    
    # Format the reminder date to match the format in the database
    formatted_reminder_date = reminder_date.strftime('%Y-%m-%d')
    
    # SQL query to fetch FDs where the maturity date is 2 days away
    cursor.execute("SELECT * FROM FixedDeposits WHERE maturity_date = ?", (formatted_reminder_date,))
    fds = cursor.fetchall()
    conn.close()
    
    return fds

# Function to send the reminder email
def send_email(bank_name, maturity_date, maturity_amount):
    if not validate_email_format(receiver_email):
        print(f"Invalid email: {receiver_email}")
        return

    subject = "FD Maturity Reminder"
    body = f"Reminder: Your FD with {bank_name} is about to mature on {maturity_date}. The maturity amount is {maturity_amount}."
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to Gmail SMTP server and send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, app_password)  # Login using the sender's email and app password
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
            print("Reminder email sent successfully.")
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check your email and app password.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to check upcoming FDs and send email reminders
def check_and_send_reminders():
    upcoming_fds = get_upcoming_fds()
    
    if upcoming_fds:
        for fd in upcoming_fds:
            bank_name = fd[1]  # Assuming column 1 is the bank name
            maturity_date = fd[4]  # Assuming column 4 is the maturity date
            maturity_amount = fd[2]  # Assuming column 2 is the maturity amount
            send_email(bank_name, maturity_date, maturity_amount)
    else:
        print("No FD is maturing in the next 2 days.")

# Call the function to check FDs and send reminders
check_and_send_reminders()
