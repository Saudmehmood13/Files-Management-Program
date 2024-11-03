import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, Text, PhotoImage, ttk

# Function to read a file and display content
def read_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
            text_area.delete(1.0, tk.END)  # Clear the text area
            text_area.insert(tk.END, content)  # Insert content into the text area
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")

# Function to write to a file
def write_file(file):
    try:
        text = text_area.get(1.0, tk.END).strip()  # Get text from text area
        with open(file, 'w') as f:
            f.write(text)
        messagebox.showinfo("Success", "The file has been written.")
    except Exception as e:
        messagebox.showerror("Error", f"Error writing to file: {e}")

# Function to append to a file
def append_file(file):
    try:
        text = text_area.get(1.0, tk.END).strip()  # Get text from text area
        with open(file, 'a') as f:
            f.write(text)
        messagebox.showinfo("Success", "The text has been appended to the file.")
    except Exception as e:
        messagebox.showerror("Error", f"Error appending to file: {e}")

# Function to delete a file
def delete_file(file):
    try:
        os.remove(file)
        messagebox.showinfo("Success", "File deleted successfully.")
        text_area.delete(1.0, tk.END)  # Clear the text area
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting file: {e}")

# Function to delete a folder
def delete_folder(folder):
    try:
        if not os.listdir(folder):  # Check if the folder is empty
            permission = messagebox.askyesno("Confirmation", "The folder is empty. Do you want to delete it?")
        else:
            permission = messagebox.askyesno("Confirmation", "The folder is NOT empty. Do you still want to delete it?")
        if permission:
            shutil.rmtree(folder)
            messagebox.showinfo("Success", "Folder deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting folder: {e}")

# File and folder selection dialog
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        perform_action(file_path)

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        perform_action(folder_path)

# Function to perform selected action
def perform_action(path):
    action = action_var.get()
    if action == "Read":
        read_file(path)
    elif action == "Write":
        write_file(path)
    elif action == "Append":
        append_file(path)
    elif action == "Delete File":
        delete_file(path)
    elif action == "Delete Folder":
        delete_folder(path)
    else:
        messagebox.showwarning("Warning", "Please select a valid action.")

# Main GUI setup
root = tk.Tk()
root.title("Professional File Management Software")
root.geometry("600x400")
root.iconbitmap('icon.ico')  # Add an icon for the window

# Styling
style = ttk.Style()
style.configure('TButton', font=('Arial', 10), padding=5)
style.configure('TLabel', font=('Arial', 12), padding=5)
style.configure('TOptionMenu', font=('Arial', 10), padding=5)

# Frame for dropdown menu and buttons
frame = ttk.Frame(root, padding=10)
frame.pack(padx=10, pady=10, fill=tk.X)

# Dropdown menu for selecting actions
action_var = tk.StringVar(root)
action_var.set("Select Action")

actions = ["Read", "Write", "Append", "Delete File", "Delete Folder"]
action_menu = ttk.OptionMenu(frame, action_var, *actions)
action_menu.grid(row=0, column=0, padx=5)

# Text area for displaying or entering text
text_area = Text(root, height=10, width=70, font=('Arial', 10))
text_area.pack(pady=10)

# Button to browse files
file_button = ttk.Button(frame, text="Browse File", command=browse_file)
file_button.grid(row=0, column=1, padx=5)

# Button to browse folders
folder_button = ttk.Button(frame, text="Browse Folder", command=browse_folder)
folder_button.grid(row=0, column=2, padx=5)

# Start the GUI loop
root.mainloop()
