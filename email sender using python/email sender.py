from email.message import EmailMessage
import ssl  
import smtplib
import tkinter as tk
from tkinter import messagebox 
    
def send_email():     
    email_sender = from_entry.get()    
    email_reciver = to_entry.get()
    email_password = 'your_application_specific_password'  # Replace with your application-specific password

    subject = subject_entry.get()  
    body = body_entry.get("1.0", tk.END) 
 
# replace your detail

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        try:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciver, em.as_string())
            messagebox.showinfo("Success", "Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Failed to authenticate. Please check your email and password.")

# Create the GUI window
window = tk.Tk()
window.title("Email Sender")
window.geometry("1000x1000")
window.resizable(False, False)

# From Label and Textbox
from_label = tk.Label(window, text="From:")
from_label.pack(pady=5)
from_entry = tk.Entry(window, font=("Georgia", 30), fg="red")
from_entry.pack(pady=5)

# To Label and Textbox
to_label = tk.Label(window, text="To:")
to_label.pack(pady=5)
to_entry = tk.Entry(window, font=("Georgia", 30), fg="red")
to_entry.pack(pady=5)

# Subject Label and Textbox
subject_label = tk.Label(window, text="Subject:")
subject_label.pack(pady=5)
subject_entry = tk.Entry(window, font=("Georgia", 30), fg="red")
subject_entry.pack(pady=5)

# Body Label and Textbox
body_label = tk.Label(window, text="Body:")
body_label.pack(pady=5)
body_entry = tk.Text(window, height=10, width=40, font=("Georgia", 30), fg="red")
body_entry.pack(pady=5)

# Send Email Button
send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack(pady=10)

# Run the GUI
window.mainloop()
