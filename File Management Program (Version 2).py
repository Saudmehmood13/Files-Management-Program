import os
import shutil

def filemanagment():
    file = input("Please enter the location of a file or folder: ")
    while True:
        #checks if the file exists or not
        if not os.path.exists(file):
            print("This location does not exist.")
            file = input("Please enter a valid location of a file or folder: ")
        else:
            if os.path.isfile(file):
                task = input("What do you want to do with this file? (Available functions: Read, Write, Update, Rename, Copy, Move, Delete): ").lower()

                #file reading function
                if task == "read":
                    with open (file) as f:
                        print(f.read())
                        break
                
                #file writing function
                elif task == "write":
                    text = input("Enter the text you want to write in this file: ")
                    with open(file, 'w') as f:
                        f.write(text)
                        print("The file has been written")
                        break

                #file copy/paste function
                elif task == "copy":
                    destination = input("Enter the location where you want to paste this file: ")
                    shutil.copy2(file, destination)
                    print("The file have been pasted")
                    break

                #file cut/paste function
                elif task == "move":
                    try:
                        destination = input("Enter the location where you want to move this file (Please add the file name in the end of the path): ")
                        os.replace(file, destination)
                    except PermissionError as e:
                        print("Something went wrong, You have to enter the file name in the end of the path")
                    else:
                        print("The file has been moved")
                        break
                
                #file renaming function
                elif task == "rename":
                    rename = input("Please enter the file location again and change the file name to the new name: ")
                    os.rename(file, rename)
                    print("File renamed")
                    break
                
                #file deleting function
                elif task == "delete":
                    permission = input("Do you permenently want to delete this file?: ").lower()
                    if permission == "yes":
                        os.remove(file)
                        print("File deleted")
                        break
                    elif permission == "no":
                        print("okay")
                    else:
                        print("Something went wrong, You had to chose between yes or no")
                
                #file updating function
                elif task == "update":
                    text = input("Enter the text you want to add/update in this file: ")
                    with open(file, 'a') as f:
                        f.write(text)
                        print("The file has been written")
                        break
                else:
                    print("I don't understand, Please select from the given options")

            elif os.path.isdir(file):
                task = input("What do you want to do with this folder? (Available functions: Rename, Move, Delete): ").lower()

                #folder cut/paste function
                if task == "move":
                    try:
                        destination = input("Enter the location where you want to move this folder (Please add the folder name in the end of the path): ")
                        os.replace(file, destination)
                    except PermissionError as e:
                        print("Something went wrong, You have to enter the folder name in the end of the path")
                    else:
                        print("The folder has been moved")
                        break
                
                #folder renaming function
                elif task == "rename":
                    rename = input("Please enter the folder location again and change the folder name to the new one: ")
                    os.rename(file, rename)
                    print("Folder renamed")
                    break
                
                #folder deleting function
                elif task == "delete":
                    permission = input("Do you want to delete this folder permenantly?: ").lower()
                    if permission == "yes":
                        shutil.rmtree(file)
                        print("Folder deleted")
                        break
                    elif permission == "no":
                        print("okay")
                    else:
                        print("Something went wrong, You had to chose between yes or no")
                else:
                    print("I don't understand please select from the given options.")

filemanagment()


start_again = input("Do you want to use the File Management Program again?: ").lower()
while True:
    if start_again == "yes":
        filemanagment()
        start_again = input("Do you want to use the File Management Program again?: ").lower()
    elif start_again == "no":
        print("Okay, Bye")
        break
    else:
        start_again = input("I don't understand, please select between yes or no: ")