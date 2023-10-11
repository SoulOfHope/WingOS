import os
from subprocess import run
from time import sleep

def main(file):
    while True:
        run("clear")
        print("Simple Text Editor")
        print("[1] Create or Edit a File")
        print("[2] Read a File")
        print("[3] Exit")
        if file:
            try:
                while True:
                    content = input("Enter the content [Press Ctrl+C to save]: ")
                    input("\n\nPress Ctrl+C to save or enter to redo\n\n")
            except KeyboardInterrupt:
                print("Saving...")
                save_text_to_file(file,content)
                print("Saved!")
                e=input("Exit? [Y or N]\n\n")
                if e.upper()=="Y":
                    break
                elif e.upper()=="N":
                    pass
                else:
                    print("Bad Input: %s" % e)
        else:
            choice = input("Enter your choice: ")
            if choice == '1':
                filename = input("Enter the filename: ")  
                content = input("Enter the text: ")
                save_text_to_file(filename, content)
            elif choice == '2':
                filename = input("Enter the filename: ")
                read_file(filename)
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                sleep(3)

def save_text_to_file(filename, content):
    try:
        if os.path.exists(filename):
            with open("WingOS/wing/emulated/home/"+filename, 'w') as file:
                file.write(content)
                print(f"Saved content to {filename}")
                sleep(3)
        else:
            with open("WingOS/wing/emulated/home/"+filename, 'x') as file:
                file.write(content)
                print(f"Saved content to {filename}")
                sleep(3)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sleep(3)

def read_file(filename):
    try:
        with open("wing/emulated/home/"+filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
            input("\n\nPress enter to continue...")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sleep(3)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sleep(3)