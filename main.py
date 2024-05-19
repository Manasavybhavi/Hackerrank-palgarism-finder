import tkinter as tk
from tkinter import messagebox
from backend import run_backend  # Import the backend function

def submit():
    username = entry_username.get()
    password = entry_password.get()
    contest = entry_contest.get()
    question = entry_question.get()
    
    # Implement validation if needed
    if not username or not password or not contest or not question:
        messagebox.showwarning("Input Error", "All fields are required")
        return
    
    # Call the backend function here
    run_backend(username, password, contest, question)

app = tk.Tk()
app.title("HackerRank Automation")

tk.Label(app, text="Username:").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(app)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Password:").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(app, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Contest Name:").grid(row=2, column=0, padx=10, pady=10)
entry_contest = tk.Entry(app)
entry_contest.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="Question Name:").grid(row=3, column=0, padx=10, pady=10)
entry_question = tk.Entry(app)
entry_question.grid(row=3, column=1, padx=10, pady=10)

tk.Button(app, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=20)

app.mainloop()
