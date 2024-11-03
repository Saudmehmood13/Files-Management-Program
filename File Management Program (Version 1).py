import os
import shutil

#C:\\Users\\Zulqarnain\\Downloads\\Saud\\code\\Hello\\Hello.txt

file = input("Please enter the location of a file or folder: ")

while True:
    #checks if the file exists or not
    if not os.path.exists(file):
        print("This location does not exist.")
        file = input("Please enter a valid location of a file or folder: ")
    else:
        task = input("What do you want to do with this file? (read, write, update, copy, move, delete): ").lower()

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
            shutil.copy(file, destination)
            print("The file have been pasted")
            break

        #file cut/paste function
        elif task == "move":
            try:
                destination = input("Enter the location where you want to move this file (please add the file name in the end of the path): ")
                os.replace(file, destination)
            except PermissionError as e:
                print("Something went wrong, You have to enter the file name in the end of the path")
            else:
                print("The file has been moved")
                break
        
        #file deleting function
        elif task == "delete":
                if os.path.isfile(file) == True:
                    permission = input("Do you permenently want to delete this file?: ").lower()
                    if permission == "yes":
                        os.remove(file)
                        print("File deleted")
                        break
                    elif permission == "no":
                        print("okay")
                    else:
                        print("Something went wrong, You had to chose between yes or no")
                elif os.path.isabs(file):
                    permission = input("This folder contains files, do you want to delete it permenantly? (All data in your folder will be lost): ").lower()
                    if permission == "yes":
                        shutil.rmtree(file)
                        print("Folder deleted")
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

