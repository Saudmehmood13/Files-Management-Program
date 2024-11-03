import os
import shutil

# Function to read a file
def read_file(file):
    try:
        with open(file, 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"Error reading file: {e}")

# Function to write to a file (overwrite)
def write_file(file):
    try:
        text = input("Enter the text you want to write in this file: ")
        with open(file, 'w') as f:
            f.write(text)
        print("The file has been written.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to append to a file
def append_file(file):
    try:
        text = input("Enter the text you want to append in this file: ")
        with open(file, 'a') as f:
            f.write(text)
        print("The text has been appended to the file.")
    except Exception as e:
        print(f"Error appending to file: {e}")

# Function to copy a file
def copy_file(file):
    try:
        destination = input("Enter the location where you want to paste this file: ")
        shutil.copy2(file, destination)
        print("The file has been copied.")
    except Exception as e:
        print(f"Error copying file: {e}")

# Function to move a file
def move_file(file):
    try:
        destination = input("Enter the location where you want to move this file (Please add the file name in the end of the path): ")
        os.replace(file, destination)
        print("The file has been moved.")
    except Exception as e:
        print(f"Error moving file: {e}")

# Function to rename a file
def rename_file(file):
    try:
        new_name = input("Please enter the new name (including path) for this file: ")
        os.rename(file, new_name)
        print("File renamed.")
    except Exception as e:
        print(f"Error renaming file: {e}")

# Function to delete a file
def delete_file(file):
    try:
        permission = input("Do you want to delete this file permanently? (yes/no): ").lower()
        if permission == "yes":
            os.remove(file)
            print("File deleted.")
        else:
            print("File deletion canceled.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Function to delete a folder (with empty check)
def delete_folder(folder):
    try:
        # Check if the folder is empty
        if not os.listdir(folder):  # If the list is empty, the folder is empty
            permission = input("The folder is empty. Do you want to delete it? (yes/no): ").lower()
        else:
            permission = input("The folder is NOT empty. Do you still want to delete it? (yes/no): ").lower()

        if permission == "yes":
            shutil.rmtree(folder)
            print("Folder deleted.")
        else:
            print("Folder deletion canceled.")
    except Exception as e:
        print(f"Error deleting folder: {e}")

# Function to handle folders
def folder_operations(folder):
    while True:
        task = input("What do you want to do with this folder? (Rename, Move, Delete): ").lower()
        
        if task == "rename":
            rename_file(folder)
            break
        elif task == "move":
            move_file(folder)
            break
        elif task == "delete":
            permission = input("Do you want to delete this folder permanently? (yes/no): ").lower()
            if permission == "yes":
                delete_folder(folder)
            else:
                print("Folder deletion canceled.")
            break
        else:
            print("Invalid option. Please choose from Rename, Move, or Delete.")


# Main function to manage files and folders
def file_management():
    file = input("Please enter the location of a file or folder: ")
    while True:
        if not os.path.exists(file):
            print("This location does not exist.")
            file = input("Please enter a valid location of a file or folder: ")
        else:
            if os.path.isfile(file):
                task = input("What do you want to do with this file? (Read, Write, Append, Rename, Copy, Move, Delete): ").lower()

                if task == "read":
                    read_file(file)
                elif task == "write":
                    write_file(file)
                elif task == "append":
                    append_file(file)
                elif task == "rename":
                    rename_file(file)
                elif task == "copy":
                    copy_file(file)
                elif task == "move":
                    move_file(file)
                elif task == "delete":
                    delete_file(file)
                else:
                    print("Invalid option. Please choose from Read, Write, Append, Rename, Copy, Move, or Delete.")
                break
            elif os.path.isdir(file):
                folder_operations(file)
                break

# Loop to allow restarting the program
def main():
    while True:
        file_management()
        start_again = input("Do you want to use the File Management Program again? (yes/no): ").lower()
        if start_again == "no":
            print("Okay, Bye!")
            break
        elif start_again != "yes":
            print("Invalid input. Please choose 'yes' or 'no'.")

# Run the program
main()
